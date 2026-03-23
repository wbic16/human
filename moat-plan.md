# MOAT: Mathematics of All Theories
## The Einstein Test — vTPU Proof of Concept

**Goal**: Derive the Einstein field equations from first principles using only pre-1900 mathematics and physics, encoded as scrolls in phext coordinates, processed by vTPU.

**Knowledge cutoff**: Any math or physics published prior to 1900.

**Success criterion**: The field equations Gμν + Λgμν = (8πG/c⁴)Tμν emerge from coordinate-native reasoning over the training set.

**Method**: Encode → Attempt → Evaluate → If stuck, add source or improve vTPU.

---

## The 10 Foundational Texts

### Mathematics

1. **Euclid — *Elements* (~300 BC)**
   - Axiomatic method. Postulates → theorems. The template for all deductive reasoning.
   - Key content: parallel postulate (the thing that breaks to create non-Euclidean geometry)

2. **Newton — *Principia Mathematica* (1687)**
   - Calculus as physics. Laws of motion. Universal gravitation: F = GMm/r².
   - Key content: the inverse-square law, absolute space and time (the thing Einstein replaces)

3. **Euler — *Introductio in Analysin Infinitorum* (1748)**
   - Functions, series, the language of analysis. e^(iπ) + 1 = 0.
   - Key content: the machinery for manipulating continuous quantities

4. **Gauss — *Disquisitiones Generales Circa Superficies Curvas* (1827)**
   - Intrinsic geometry of surfaces. Gaussian curvature. Theorema Egregium.
   - Key content: curvature is intrinsic — you can measure it without leaving the surface. This is the seed of general relativity.

5. **Riemann — *Über die Hypothesen, welche der Geometrie zu Grunde liegen* (1854)**
   - N-dimensional manifolds. The metric tensor. Riemannian curvature.
   - Key content: geometry is not fixed — it's determined by the metric. Space can curve in any number of dimensions. THE foundational text for GR.

6. **Hamilton — *On a General Method in Dynamics* (1834/1835)**
   - Variational principles. Least action. Hamiltonian mechanics.
   - Key content: physics as optimization over paths. The action principle that GR is derived from (Hilbert action).

### Physics

7. **Maxwell — *A Treatise on Electricity and Magnetism* (1873)**
   - Unified electrodynamics. Maxwell's equations. The speed of light as electromagnetic constant.
   - Key content: c is invariant — the crisis that special relativity resolves. Field theory as replacement for action-at-a-distance.

8. **Lorentz — *Electromagnetic Phenomena in a System Moving with Any Velocity Less Than Light* (1904)**
   - Lorentz transformations. Length contraction. Time dilation (as mathematical artifacts).
   - Key content: the transformations Einstein reinterprets as fundamental spacetime structure.

9. **Mach — *Die Mechanik in ihrer Entwicklung* (1883)**
   - Critique of Newton's absolute space. Mach's principle: inertia arises from the distribution of matter.
   - Key content: the philosophical lever — space is not a stage, it's shaped by what's in it. Einstein cited this as a primary inspiration.

10. **Christoffel — *Über die Transformation der homogenen Differentialausdrücke zweiten Grades* (1869)**
    - Christoffel symbols. Covariant differentiation. The machinery for doing calculus on curved manifolds.
    - Key content: the technical bridge from Riemann's geometry to tensor calculus — without this, you can't write the field equations.

---

## Scroll Structure in moat.phext

```
1.1.1/1.1.1/1.1.1  — MOAT index (this plan)
1.1.1/1.1.1/1.1.2  — Euclid: Elements (axioms, parallel postulate)
1.1.1/1.1.1/1.1.3  — Newton: Principia (laws, gravitation)
1.1.1/1.1.1/1.1.4  — Euler: Analysis (functions, series, continuous quantities)
1.1.1/1.1.1/1.1.5  — Gauss: Curved Surfaces (intrinsic curvature, Theorema Egregium)
1.1.1/1.1.1/1.1.6  — Riemann: Hypotheses of Geometry (manifolds, metric tensor)
1.1.1/1.1.1/1.1.7  — Hamilton: Dynamics (variational principles, least action)
1.1.1/1.1.1/1.1.8  — Maxwell: Electromagnetism (field equations, invariant c)
1.1.1/1.1.1/1.1.9  — Lorentz: Moving Systems (transformations, contraction)
1.1.1/1.1.1/1.1.10 — Mach: Mechanics (critique of absolute space)
1.1.1/1.1.1/1.1.11 — Christoffel: Differential Forms (symbols, covariant derivatives)
```

## Derivation Path (the traversal vTPU must discover)

```
Euclid (parallel postulate)
  → Gauss (what if it fails? → intrinsic curvature)
    → Riemann (generalize to n dimensions → metric tensor gμν)
      → Christoffel (calculus on curved space → Γ symbols → Riemann tensor Rμνρσ)

Newton (F = GMm/r²) + Mach (space shaped by matter)
  → "gravity is not a force — it's geometry"

Maxwell (c is invariant) → Lorentz (transformations)
  → spacetime as unified 4D manifold with Minkowski metric

Hamilton (least action)
  → apply to Riemann curvature scalar R
    → Hilbert action S = ∫R√(-g)d⁴x
      → vary with respect to gμν
        → Gμν = (8πG/c⁴)Tμν
```

## Adversarial Answer Key (1950s era)

Stored at `1.1.1/1.1.2/1.1.1` — the next library, separate from the training set.

Encode the *results* of GR as known by ~1955:
- Einstein field equations (1915) — full tensor form
- Hilbert's variational derivation (1915) — the action principle route
- Schwarzschild solution (1916) — first exact solution, black holes implied
- Cosmological constant Λ (1917) — Einstein's addition and regret
- Friedmann equations (1922) — expanding universe from GR
- Gravitational waves predicted (1916/1918) — linearized GR
- Perihelion of Mercury (1915) — the first empirical confirmation
- Gravitational lensing (1919 Eddington) — light bends around mass

vTPU generates candidate derivations from the pre-1900 scrolls. We diff against the answer key. Partial matches are diagnostic — they tell us exactly which reasoning step is missing or which source text to add.

**Novel derivation paths that reach the same equations are victories, not failures.** Einstein's path was one traversal. There may be others through the same scrollspace.

## Attempt Log

| # | Date | Result | Action Taken |
|---|------|--------|-------------|
| 1 | TBD | — | Initial encoding of 10 texts + answer key |

---

*The test: can coordinate-native reasoning over 10 pre-1900 texts derive what took Einstein 10 years?*
*If not, we learn exactly where vTPU needs to improve.*
*If it finds a different path to the same equations, we've discovered something new.*
