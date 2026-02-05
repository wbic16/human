#!/usr/bin/env python3
"""
phext_image.py - Semantic Image Encoder/Decoder using Phext 11D Coordinates
===========================================================================

Maps pixel data into phext's 11-dimensional coordinate space where:
  - Library (dim 9) = Y spatial position
  - Series  (dim 7) = X spatial position  
  - Remaining 7 dimensions encode MEANING, not just color:
    Collection (dim 8) = Hue Archetype
    Volume     (dim 6) = Luminance Band
    Book       (dim 5) = Saturation Class
    Chapter    (dim 4) = Texture Context
    Section    (dim 3) = Semantic Domain
    Scroll     (dim 2) = Symbolic Register
    Line       (dim 1) = Fine Detail

Phext's negative space encoding means we only store non-empty semantic
coordinates. A mostly-blue sky image compresses beautifully because
most pixels share the same semantic neighborhood.

The lookup tables below are the "tarpit of human knowledge" -
mapping raw pixel data to culturally-loaded semantic categories.
"""

import json
import math
import struct
import colorsys
from collections import defaultdict
from dataclasses import dataclass, field
from typing import Optional

# ============================================================================
# PHEXT DELIMITERS (ASCII control codes)
# ============================================================================
# These are the actual phext dimensional separators
PHEXT_DELIMITERS = {
    'line_break':       '\n',       # 0x0A - separates lines (dim 1)
    'scroll_break':     '\x17',     # 0x17 - separates scrolls (dim 2)
    'section_break':    '\x18',     # 0x18 - separates sections (dim 3)
    'chapter_break':    '\x19',     # 0x19 - separates chapters (dim 4)
    'book_break':       '\x1A',     # 0x1A - separates books (dim 5)
    'volume_break':     '\x1B',     # 0x1B - separates volumes (dim 6)
    'collection_break': '\x1C',     # 0x1C - separates collections (dim 7/series)
    'series_break':     '\x1D',     # 0x1D - separates series (dim 8)
    'shelf_break':      '\x1E',     # 0x1E - separates shelves (dim 9)
    'library_break':    '\x1F',     # 0x1F - separates libraries (dim 10)
}

# ============================================================================
# THE TARPIT OF HUMAN KNOWLEDGE: LOOKUP TABLES
# ============================================================================
# Each table maps a quantized index (0-15) to a semantic label.
# The tables encode 30,000 years of human color/meaning association.
# 16 bins per dimension = 16^7 = 268 million possible semantic addresses.

HUE_ARCHETYPES = {
    #  idx: (name, description, cultural_root)
    0:  ("void",       "absence of hue, the unnamed",           "paleolithic cave darkness"),
    1:  ("arterial",   "the red of opened veins",               "ochre handprints at Lascaux"),
    2:  ("ember",      "red-orange of dying fires",             "hearthfire, Prometheus"),
    3:  ("saffron",    "precious orange-yellow",                "spice routes, Buddhist robes"),
    4:  ("auroral",    "pure yellow, solar direct",             "Ra, Amaterasu, gold leaf"),
    5:  ("verdant",    "yellow-green of new growth",            "spring equinox, fertility"),
    6:  ("chlorophyl", "true green, photosynthetic",            "the engine of all terrestrial life"),
    7:  ("verdigris",  "blue-green of aged copper",             "Statue of Liberty, patina of time"),
    8:  ("cerulean",   "true blue, sky-at-zenith",              "lapis lazuli, ultramarine, Mary's robe"),
    9:  ("indigo",     "deep blue-violet",                      "Indian dye trade, the space between"),
    10: ("amethyst",   "violet, the alchemical",                "Dionysus, transmutation, royalty"),
    11: ("magenta",    "red-violet, the impossible",            "no spectral wavelength, mind-only color"),
    12: ("rose",       "pink, diluted arterial",                "tenderness, flesh, vulnerability"),
    13: ("umber",      "earth tone, soil and bark",             "raw pigment, the ground beneath"),
    14: ("silver",     "metallic neutral, moonlight",           "lunar cycles, mirrors, Mercury"),
    15: ("bone",       "warm white, organic neutral",           "ivory, parchment, the calcified"),
}

LUMINANCE_BANDS = {
    0:  ("abyss",      "true black, event horizon"),
    1:  ("deep_earth", "coal seam, cave interior"),
    2:  ("umbra",      "shadow core, eclipse dark"),
    3:  ("penumbra",   "shadow edge, twilight"),
    4:  ("dusk",       "civil twilight, gloaming"),
    5:  ("shade",      "north-facing wall, overcast"),
    6:  ("ambient",    "diffuse indoor light"),
    7:  ("overcast",   "cloud-filtered daylight"),
    8:  ("daylight",   "standard illumination"),
    9:  ("bright",     "direct sunlight, full exposure"),
    10: ("radiant",    "reflective surface, snow"),
    11: ("glare",      "near-painful brightness"),
    12: ("blinding",   "welding arc, sun-on-water"),
    13: ("bleached",   "overexposed, lost detail"),
    14: ("spectral",   "glowing from within"),
    15: ("white_hole", "pure emission, total luminance"),
}

SATURATION_CLASSES = {
    0:  ("ash",        "fully desaturated, spent"),
    1:  ("fog",        "barely there, memory of color"),
    2:  ("dust",       "muted, sun-faded"),
    3:  ("linen",      "natural, undyed"),
    4:  ("weathered",  "exposure-worn, patinated"),
    5:  ("matte",      "moderate, clay-like"),
    6:  ("earthen",    "natural pigment saturation"),
    7:  ("dyed",       "processed, deliberate color"),
    8:  ("painted",    "artist-mixed intensity"),
    9:  ("vivid",      "fresh fruit, flower petal"),
    10: ("electric",   "neon-adjacent, vibrating"),
    11: ("saturated",  "maximum natural chroma"),
    12: ("synthetic",  "beyond nature, plastic"),
    13: ("laser",      "coherent, single-wavelength"),
    14: ("psychedelic", "oversaturated, hallucinatory"),
    15: ("impossible", "super-stimulus, chroma overflow"),
}

TEXTURE_SEEDS = {
    0:  ("smooth",     "polished, frictionless"),
    1:  ("liquid",     "flowing, reflective surface"),
    2:  ("mist",       "gaseous, boundary-less"),
    3:  ("silk",       "fine-woven, light-catching"),
    4:  ("skin",       "organic membrane, porous"),
    5:  ("bark",       "rough organic, fractured"),
    6:  ("stone",      "mineral, granular"),
    7:  ("crystal",    "ordered lattice, faceted"),
    8:  ("woven",      "textile, regular pattern"),
    9:  ("fractal",    "self-similar at all scales"),
    10: ("eroded",     "shaped by time and flow"),
    11: ("shattered",  "broken geometry, sharp"),
    12: ("tangled",    "chaotic organic, roots/nerves"),
    13: ("pixelated",  "discrete, quantized"),
    14: ("static",     "random noise, entropic"),
    15: ("void_tex",   "textureless, undefined"),
}

SEMANTIC_DOMAINS = {
    0:  ("void_sem",   "nothing, absence, null"),
    1:  ("flesh",      "animal tissue, living body"),
    2:  ("vegetation", "plant matter, growing things"),
    3:  ("water",      "liquid, ocean, rain, tears"),
    4:  ("sky",        "atmosphere, weather, breath"),
    5:  ("earth",      "soil, ground, planet-skin"),
    6:  ("stone",      "mineral, mountain, bone-of-world"),
    7:  ("fire",       "plasma, combustion, star-stuff"),
    8:  ("metal",      "refined element, forged"),
    9:  ("wood",       "dead vegetation, structured"),
    10: ("glass",      "transparent solid, fragile"),
    11: ("fabric",     "woven material, clothing"),
    12: ("light_sem",  "photons, glow, illumination"),
    13: ("shadow_sem", "absence of light, negative space"),
    14: ("text",       "written symbol, glyph"),
    15: ("machine",    "artificial, constructed"),
}

SYMBOLIC_REGISTERS = {
    0:  ("mundane",    "ordinary, unremarkable"),
    1:  ("domestic",   "home, comfort, safety"),
    2:  ("fertile",    "growth, potential, spring"),
    3:  ("nurturing",  "care, warmth, mother"),
    4:  ("playful",    "joy, lightness, child"),
    5:  ("erotic",     "desire, attraction, heat"),
    6:  ("martial",    "conflict, strength, iron"),
    7:  ("sacred",     "holy, set-apart, numinous"),
    8:  ("liminal",    "threshold, between, transitional"),
    9:  ("melancholy", "loss, autumn, memory"),
    10: ("ominous",    "foreboding, approaching danger"),
    11: ("sublime",    "terrible beauty, awe"),
    12: ("alien",      "inhuman, uncanny, other"),
    13: ("ancient",    "deep time, fossil, ruin"),
    14: ("electric_s", "modern, technological, wired"),
    15: ("void_sym",   "nihil, entropy, heat death"),
}

FINE_DETAIL = {
    # Sub-classification within domain - 16 levels of specificity
    # This is the "last mile" of meaning
    0:  ("null",       "no further detail"),
    1:  ("core",       "center, essence, heart"),
    2:  ("edge",       "boundary, transition, border"),
    3:  ("gradient",   "blending, morphing, fade"),
    4:  ("highlight",  "focal point, brightest"),
    5:  ("accent",     "punctuation, emphasis"),
    6:  ("background", "recessive, supporting"),
    7:  ("pattern_a",  "repeating element A"),
    8:  ("pattern_b",  "repeating element B"),
    9:  ("anomaly",    "break in pattern, surprise"),
    10: ("reflection", "mirror, echo, doubled"),
    11: ("depth_cue",  "perspective, distance"),
    12: ("motion_blur","movement, time-smeared"),
    13: ("focus",      "sharp, attended to"),
    14: ("bokeh",      "out of focus, dreamy"),
    15: ("artifact",   "compression, noise, error"),
}

ALL_TABLES = [
    ("hue_archetype",     HUE_ARCHETYPES),
    ("luminance_band",    LUMINANCE_BANDS),
    ("saturation_class",  SATURATION_CLASSES),
    ("texture_seed",      TEXTURE_SEEDS),
    ("semantic_domain",   SEMANTIC_DOMAINS),
    ("symbolic_register", SYMBOLIC_REGISTERS),
    ("fine_detail",       FINE_DETAIL),
]


# ============================================================================
# SEMANTIC COORDINATE
# ============================================================================

@dataclass
class SemanticPixel:
    """A pixel expressed as a 7D meaning coordinate."""
    hue_archetype:     int = 0   # Collection dimension
    luminance_band:    int = 0   # Volume dimension
    saturation_class:  int = 0   # Book dimension
    texture_seed:      int = 0   # Chapter dimension
    semantic_domain:   int = 0   # Section dimension
    symbolic_register: int = 0   # Scroll dimension
    fine_detail:       int = 0   # Line dimension

    def to_tuple(self):
        return (self.hue_archetype, self.luminance_band, self.saturation_class,
                self.texture_seed, self.semantic_domain, self.symbolic_register,
                self.fine_detail)

    def describe(self):
        """Human-readable semantic description of this pixel."""
        return {
            'hue':        HUE_ARCHETYPES[self.hue_archetype][0],
            'luminance':  LUMINANCE_BANDS[self.luminance_band][0],
            'saturation': SATURATION_CLASSES[self.saturation_class][0],
            'texture':    TEXTURE_SEEDS[self.texture_seed][0],
            'domain':     SEMANTIC_DOMAINS[self.semantic_domain][0],
            'symbol':     SYMBOLIC_REGISTERS[self.symbolic_register][0],
            'detail':     FINE_DETAIL[self.fine_detail][0],
        }

    def to_rgb(self):
        """Decode back to approximate RGB via the reverse lookup."""
        return semantic_to_rgb(self)

    def semantic_distance(self, other: 'SemanticPixel') -> float:
        """Euclidean distance in 7D semantic space."""
        a, b = self.to_tuple(), other.to_tuple()
        return math.sqrt(sum((x - y) ** 2 for x, y in zip(a, b)))


# ============================================================================
# ENCODER: RGB → Semantic Coordinate
# ============================================================================

def rgb_to_hue_archetype(r, g, b) -> int:
    """Map RGB to hue archetype index (0-15)."""
    h, s, v = colorsys.rgb_to_hsv(r / 255, g / 255, b / 255)

    # Handle achromatic cases
    if s < 0.08:
        if v < 0.1:
            return 0   # void
        elif v > 0.9:
            return 15  # bone
        else:
            return 14  # silver

    # Handle earth tones (low saturation warm hues)
    if s < 0.3 and 0.02 < h < 0.12:
        return 13  # umber

    # Map hue angle (0-1) to archetype
    # Hue wheel: 0=red, 0.083=orange, 0.167=yellow, 0.333=green,
    #            0.5=cyan, 0.667=blue, 0.833=purple
    hue_map = [
        (0.02,  1),   # arterial (red)
        (0.06,  2),   # ember (red-orange)
        (0.11,  3),   # saffron (orange-yellow)
        (0.18,  4),   # auroral (yellow)
        (0.25,  5),   # verdant (yellow-green)
        (0.40,  6),   # chlorophyl (green)
        (0.48,  7),   # verdigris (blue-green)
        (0.58,  8),   # cerulean (blue)
        (0.70,  9),   # indigo (deep blue)
        (0.78,  10),  # amethyst (violet)
        (0.88,  11),  # magenta (red-violet)
        (0.95,  12),  # rose (pink-ish)
        (1.01,  1),   # wraps back to arterial
    ]

    for threshold, idx in hue_map:
        if h < threshold:
            return idx
    return 1  # default arterial


def rgb_to_luminance_band(r, g, b) -> int:
    """Map perceived luminance to band index (0-15)."""
    # ITU-R BT.709 perceptual luminance
    lum = (0.2126 * r + 0.7152 * g + 0.0722 * b) / 255.0
    return min(15, int(lum * 16))


def rgb_to_saturation_class(r, g, b) -> int:
    """Map saturation to class index (0-15)."""
    _, s, _ = colorsys.rgb_to_hsv(r / 255, g / 255, b / 255)
    return min(15, int(s * 16))


def rgb_to_texture_seed(r, g, b, neighbors=None) -> int:
    """
    Map local pixel context to texture seed.
    Without neighbors, uses a luminance-based heuristic.
    With neighbors (list of (r,g,b) tuples), computes local variance.
    """
    if neighbors is None:
        # Fallback: use luminance fractional part as texture hint
        lum = (0.2126 * r + 0.7152 * g + 0.0722 * b) / 255.0
        # Low luminance variance → smooth, high → rough
        return min(15, int((lum * 7.3) % 1.0 * 16))

    # Compute local variance from neighborhood
    lums = [(0.2126 * nr + 0.7152 * ng + 0.0722 * nb) / 255.0
            for nr, ng, nb in neighbors]
    mean_l = sum(lums) / len(lums)
    variance = sum((l - mean_l) ** 2 for l in lums) / len(lums)

    if variance < 0.001:   return 0   # smooth
    elif variance < 0.005: return 3   # silk
    elif variance < 0.01:  return 4   # skin
    elif variance < 0.03:  return 6   # stone
    elif variance < 0.06:  return 5   # bark
    elif variance < 0.1:   return 9   # fractal
    elif variance < 0.2:   return 11  # shattered
    else:                  return 14  # static


def rgb_to_semantic_domain(r, g, b) -> int:
    """
    Infer semantic domain from color.
    This is the most "unhinged" mapping - pure heuristic color → meaning.
    """
    h, s, v = colorsys.rgb_to_hsv(r / 255, g / 255, b / 255)

    if v < 0.05:
        return 13  # shadow
    if v > 0.95 and s < 0.05:
        return 12  # light

    # Sky detection: blue, desaturated-to-moderate, mid-to-high value
    if 0.5 < h < 0.7 and s < 0.6 and v > 0.5:
        return 4  # sky

    # Water: blue-green, moderate saturation
    if 0.45 < h < 0.65 and 0.2 < s < 0.7 and 0.2 < v < 0.7:
        return 3  # water

    # Vegetation: green
    if 0.2 < h < 0.45 and s > 0.15 and 0.1 < v < 0.8:
        return 2  # vegetation

    # Fire: red-orange-yellow, high saturation, high value
    if (h < 0.12 or h > 0.95) and s > 0.6 and v > 0.6:
        return 7  # fire

    # Flesh: warm hues, moderate saturation
    if (h < 0.08 or h > 0.92) and 0.15 < s < 0.6 and 0.3 < v < 0.9:
        return 1  # flesh

    # Earth: low saturation warm
    if h < 0.15 and s < 0.4 and 0.1 < v < 0.5:
        return 5  # earth

    # Metal: low saturation, mid-high value
    if s < 0.15 and 0.3 < v < 0.85:
        return 8  # metal

    # Wood: orange-brown
    if 0.05 < h < 0.12 and 0.2 < s < 0.6 and 0.15 < v < 0.55:
        return 9  # wood

    return 0  # void (unclassified)


def rgb_to_symbolic_register(r, g, b, semantic_domain=None) -> int:
    """
    Infer symbolic weight from color + domain context.
    This is where it gets truly subjective - mapping color to FEELING.
    """
    h, s, v = colorsys.rgb_to_hsv(r / 255, g / 255, b / 255)

    # Very dark = ominous or void
    if v < 0.1:
        return 15  # void_sym

    # Very bright + saturated = sublime or electric
    if v > 0.85 and s > 0.7:
        if h < 0.1 or h > 0.9:  # reds
            return 5 if s > 0.5 else 6  # erotic or martial
        if 0.55 < h < 0.75:  # blues
            return 7  # sacred
        return 14  # electric

    # Warm + soft = domestic/nurturing
    if 0.02 < h < 0.12 and s < 0.4 and 0.4 < v < 0.8:
        return 1  # domestic

    # Green + moderate = fertile
    if 0.2 < h < 0.45 and s > 0.2:
        return 2  # fertile

    # Blue + desaturated = melancholy
    if 0.55 < h < 0.7 and s < 0.3:
        return 9  # melancholy

    # Purple = liminal
    if 0.7 < h < 0.85:
        return 8  # liminal

    # Grays = mundane
    if s < 0.1:
        return 0  # mundane

    return 0  # mundane default


def rgb_to_fine_detail(r, g, b, x=0, y=0, width=1, height=1) -> int:
    """
    Fine detail classification based on spatial position and value.
    """
    _, _, v = colorsys.rgb_to_hsv(r / 255, g / 255, b / 255)

    # Edge detection (simple: near image boundary)
    margin = 0.05
    nx, ny = x / max(width, 1), y / max(height, 1)
    if nx < margin or nx > (1 - margin) or ny < margin or ny > (1 - margin):
        return 2  # edge

    # Highlight detection
    if v > 0.95:
        return 4  # highlight

    # Center-weighted = core
    cx, cy = abs(nx - 0.5), abs(ny - 0.5)
    if cx < 0.15 and cy < 0.15:
        return 1  # core

    # Background detection (low contrast areas would go here with context)
    if v < 0.2:
        return 6  # background

    return 0  # null


def encode_pixel(r, g, b, x=0, y=0, width=1, height=1, neighbors=None) -> SemanticPixel:
    """Encode a single RGB pixel into a 7D semantic coordinate."""
    domain = rgb_to_semantic_domain(r, g, b)
    return SemanticPixel(
        hue_archetype     = rgb_to_hue_archetype(r, g, b),
        luminance_band    = rgb_to_luminance_band(r, g, b),
        saturation_class  = rgb_to_saturation_class(r, g, b),
        texture_seed      = rgb_to_texture_seed(r, g, b, neighbors),
        semantic_domain   = domain,
        symbolic_register = rgb_to_symbolic_register(r, g, b, domain),
        fine_detail        = rgb_to_fine_detail(r, g, b, x, y, width, height),
    )


# ============================================================================
# DECODER: Semantic Coordinate → RGB
# ============================================================================
# The reverse mapping. Note: this is LOSSY by design.
# Multiple RGB values map to the same semantic coordinate.
# The decoder produces a "canonical" RGB for each semantic address.

# Hue archetype → representative hue angle (0-360)
ARCHETYPE_HUES = {
    0: None,    # void - achromatic
    1: 0,       # arterial
    2: 20,      # ember
    3: 38,      # saffron
    4: 55,      # auroral
    5: 80,      # verdant
    6: 120,     # chlorophyl
    7: 170,     # verdigris
    8: 210,     # cerulean
    9: 245,     # indigo
    10: 275,    # amethyst
    11: 310,    # magenta
    12: 340,    # rose
    13: 25,     # umber (low sat)
    14: None,   # silver - achromatic
    15: None,   # bone - achromatic
}

def semantic_to_rgb(sp: SemanticPixel) -> tuple:
    """Decode semantic coordinate back to representative RGB."""
    # Reconstruct luminance (0-1)
    v = (sp.luminance_band + 0.5) / 16.0

    # Reconstruct saturation (0-1)
    s = (sp.saturation_class + 0.5) / 16.0

    # Get hue
    hue_deg = ARCHETYPE_HUES.get(sp.hue_archetype)

    if hue_deg is None:
        # Achromatic
        if sp.hue_archetype == 0:    # void
            val = int(v * 40)  # dark
        elif sp.hue_archetype == 14:  # silver
            val = int(160 + v * 60)
        else:  # bone
            val = int(220 + v * 35)
        return (min(255, val), min(255, val), min(255, val))

    # Convert HSV to RGB
    h = hue_deg / 360.0

    # For umber, reduce saturation
    if sp.hue_archetype == 13:
        s = min(s, 0.4)
        v = min(v, 0.5)

    r, g, b = colorsys.hsv_to_rgb(h, min(1.0, s), min(1.0, v))
    return (int(r * 255), int(g * 255), int(b * 255))


# ============================================================================
# PHEXT ENCODING: Semantic Grid → Phext Document
# ============================================================================

def encode_image_to_phext(pixels, width, height) -> str:
    """
    Encode a 2D grid of RGB pixels into a phext document.
    
    Uses NEGATIVE SPACE encoding: pixels that share the same semantic
    coordinate are grouped, and only the transitions are stored.
    
    Structure:
      Library[y].Series[x] → Collection[hue].Volume[lum].Book[sat].
                               Chapter[tex].Section[dom].Scroll[sym].Line[detail]
    
    The content at each address is a compact token representing the
    semantic coordinate, enabling reconstruction.
    """
    # First pass: encode all pixels
    semantic_grid = []
    for y in range(height):
        row = []
        for x in range(width):
            idx = (y * width + x) * 3
            r, g, b = pixels[idx], pixels[idx + 1], pixels[idx + 2]

            # Get neighbors for texture analysis
            neighbors = []
            for dy in [-1, 0, 1]:
                for dx in [-1, 0, 1]:
                    if dy == 0 and dx == 0:
                        continue
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < width and 0 <= ny < height:
                        ni = (ny * width + nx) * 3
                        neighbors.append((pixels[ni], pixels[ni+1], pixels[ni+2]))

            sp = encode_pixel(r, g, b, x, y, width, height, neighbors)
            row.append(sp)
        semantic_grid.append(row)

    # Second pass: build phext document using negative space
    # Group consecutive pixels with same semantic coordinate
    doc_parts = []
    for y in range(height):
        row_parts = []
        run_start = 0
        run_coord = semantic_grid[y][0].to_tuple()

        for x in range(1, width):
            current = semantic_grid[y][x].to_tuple()
            if current != run_coord:
                # Emit the run
                row_parts.append(_encode_run(run_coord, run_start, x - 1))
                run_start = x
                run_coord = current

        # Emit final run
        row_parts.append(_encode_run(run_coord, run_start, width - 1))

        # Join runs within a row with collection breaks (x-axis = series)
        doc_parts.append(PHEXT_DELIMITERS['collection_break'].join(row_parts))

    # Join rows with library breaks (y-axis = library)
    phext_doc = PHEXT_DELIMITERS['library_break'].join(doc_parts)

    return phext_doc


def _encode_run(coord_tuple, start_x, end_x):
    """
    Encode a run of identical semantic pixels.
    Format: "start:end|h.l.s.t.d.y.f"
    The negative space magic: a 200-pixel sky run becomes ONE entry.
    """
    hue, lum, sat, tex, dom, sym, detail = coord_tuple
    coord_str = f"{hue:x}{lum:x}{sat:x}{tex:x}{dom:x}{sym:x}{detail:x}"
    if start_x == end_x:
        return f"{start_x}|{coord_str}"
    return f"{start_x}:{end_x}|{coord_str}"


def decode_phext_to_image(phext_doc: str, width: int, height: int) -> list:
    """
    Decode a phext document back into RGB pixel data.
    Returns flat list of [r, g, b, r, g, b, ...].
    """
    pixels = [0] * (width * height * 3)

    rows = phext_doc.split(PHEXT_DELIMITERS['library_break'])

    for y, row_data in enumerate(rows):
        if y >= height:
            break
        runs = row_data.split(PHEXT_DELIMITERS['collection_break'])

        for run in runs:
            if '|' not in run:
                continue

            pos_part, coord_str = run.split('|', 1)

            if ':' in pos_part:
                start_x, end_x = map(int, pos_part.split(':'))
            else:
                start_x = end_x = int(pos_part)

            # Decode semantic coordinate from hex string
            if len(coord_str) >= 7:
                sp = SemanticPixel(
                    hue_archetype     = int(coord_str[0], 16),
                    luminance_band    = int(coord_str[1], 16),
                    saturation_class  = int(coord_str[2], 16),
                    texture_seed      = int(coord_str[3], 16),
                    semantic_domain   = int(coord_str[4], 16),
                    symbolic_register = int(coord_str[5], 16),
                    fine_detail       = int(coord_str[6], 16),
                )
                r, g, b = sp.to_rgb()

                for x in range(start_x, min(end_x + 1, width)):
                    idx = (y * width + x) * 3
                    pixels[idx] = r
                    pixels[idx + 1] = g
                    pixels[idx + 2] = b

    return pixels


# ============================================================================
# ANALYSIS & STATS
# ============================================================================

def analyze_image_semantics(pixels, width, height) -> dict:
    """
    Produce a semantic analysis of an image:
    - Dominant hue archetypes
    - Luminance distribution
    - Semantic domain breakdown
    - Symbolic register histogram
    - Compression ratio from run-length encoding
    """
    counters = {name: defaultdict(int) for name, _ in ALL_TABLES}
    total_pixels = width * height
    unique_coords = set()
    runs = 0

    for y in range(height):
        prev_coord = None
        for x in range(width):
            idx = (y * width + x) * 3
            r, g, b = pixels[idx], pixels[idx+1], pixels[idx+2]
            sp = encode_pixel(r, g, b, x, y, width, height)
            coord = sp.to_tuple()
            unique_coords.add(coord)

            if coord != prev_coord:
                runs += 1
                prev_coord = coord

            counters['hue_archetype'][sp.hue_archetype] += 1
            counters['luminance_band'][sp.luminance_band] += 1
            counters['saturation_class'][sp.saturation_class] += 1
            counters['texture_seed'][sp.texture_seed] += 1
            counters['semantic_domain'][sp.semantic_domain] += 1
            counters['symbolic_register'][sp.symbolic_register] += 1
            counters['fine_detail'][sp.fine_detail] += 1

    # Build human-readable results
    tables = {
        'hue_archetype': HUE_ARCHETYPES,
        'luminance_band': LUMINANCE_BANDS,
        'saturation_class': SATURATION_CLASSES,
        'texture_seed': TEXTURE_SEEDS,
        'semantic_domain': SEMANTIC_DOMAINS,
        'symbolic_register': SYMBOLIC_REGISTERS,
        'fine_detail': FINE_DETAIL,
    }

    result = {
        'total_pixels': total_pixels,
        'unique_semantic_coords': len(unique_coords),
        'semantic_runs': runs,
        'compression_ratio': total_pixels / max(runs, 1),
        'dimensions': {}
    }

    for dim_name, table in tables.items():
        dim_dist = []
        for idx in sorted(counters[dim_name].keys()):
            count = counters[dim_name][idx]
            name = table[idx][0]
            pct = count / total_pixels * 100
            dim_dist.append({
                'index': idx,
                'name': name,
                'count': count,
                'percentage': round(pct, 1)
            })
        # Sort by count descending
        dim_dist.sort(key=lambda x: -x['count'])
        result['dimensions'][dim_name] = dim_dist

    return result


# ============================================================================
# DEMO / SELF-TEST
# ============================================================================

def demo():
    """Demonstrate the encoder with some test pixels."""
    test_pixels = [
        (255, 0, 0,     "pure red"),
        (0, 128, 255,   "sky blue"),
        (34, 139, 34,   "forest green"),
        (255, 165, 0,   "orange"),
        (10, 10, 10,    "near black"),
        (245, 222, 179, "wheat/skin tone"),
        (128, 0, 128,   "purple"),
        (255, 255, 255, "white"),
    ]

    print("=" * 78)
    print("PHEXT IMAGE SEMANTIC ENCODER - Demo")
    print("=" * 78)

    for r, g, b, name in test_pixels:
        sp = encode_pixel(r, g, b)
        desc = sp.describe()
        reconstructed = sp.to_rgb()
        print(f"\n  {name} ({r},{g},{b}) →")
        print(f"    hue={desc['hue']:12s}  lum={desc['luminance']:12s}  "
              f"sat={desc['saturation']:12s}")
        print(f"    tex={desc['texture']:12s}  dom={desc['domain']:12s}  "
              f"sym={desc['symbol']:12s}  detail={desc['detail']}")
        print(f"    → reconstructed: {reconstructed}")
        print(f"    → hex coord: {''.join(f'{x:x}' for x in sp.to_tuple())}")

    # Test run-length encoding with synthetic "sky" image
    print("\n" + "=" * 78)
    print("NEGATIVE SPACE COMPRESSION TEST: 32x8 synthetic sky")
    print("=" * 78)

    w, h = 32, 8
    sky_pixels = []
    for y in range(h):
        for x in range(w):
            # Gradient blue sky
            blue = 200 + int(55 * (1 - y / h))
            green = 150 + int(50 * (1 - y / h))
            red = 100 + int(30 * x / w)
            sky_pixels.extend([min(255, red), min(255, green), min(255, blue)])

    phext_doc = encode_image_to_phext(sky_pixels, w, h)
    raw_size = w * h * 3  # RGB bytes
    phext_size = len(phext_doc.encode('utf-8'))

    print(f"  Raw RGB size:   {raw_size} bytes")
    print(f"  Phext doc size: {phext_size} bytes")
    print(f"  Ratio:          {phext_size/raw_size:.2f}x "
          f"({'smaller' if phext_size < raw_size else 'larger'})")

    # Analyze
    analysis = analyze_image_semantics(sky_pixels, w, h)
    print(f"  Unique semantic coords: {analysis['unique_semantic_coords']}")
    print(f"  Semantic runs: {analysis['semantic_runs']} "
          f"(from {w*h} pixels = {analysis['compression_ratio']:.1f}x compression)")

    print(f"\n  Top semantic domains:")
    for entry in analysis['dimensions']['semantic_domain'][:3]:
        print(f"    {entry['name']:12s}: {entry['percentage']:5.1f}%")

    print(f"\n  Top symbolic registers:")
    for entry in analysis['dimensions']['symbolic_register'][:3]:
        print(f"    {entry['name']:12s}: {entry['percentage']:5.1f}%")

    # Roundtrip test
    decoded = decode_phext_to_image(phext_doc, w, h)
    print(f"\n  Roundtrip decode: {len(decoded)//3} pixels recovered")

    # Show a snippet of the phext doc
    print(f"\n  Phext document (first 200 chars):")
    preview = phext_doc[:200].replace('\x17', '⟨scroll⟩').replace('\x18', '⟨section⟩')
    preview = preview.replace('\x19', '⟨chapter⟩').replace('\x1a', '⟨book⟩')
    preview = preview.replace('\x1b', '⟨volume⟩').replace('\x1c', '⟨col⟩')
    preview = preview.replace('\x1d', '⟨series⟩').replace('\x1e', '⟨shelf⟩')
    preview = preview.replace('\x1f', '⟨lib⟩')
    print(f"  {preview}...")


if __name__ == '__main__':
    demo()
