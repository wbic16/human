import matplotlib.pyplot as plt
import numpy as np
import scipy.io.wavfile as wav
from pydub import AudioSegment

# Load the MP3 and convert to WAV in memory
audio = AudioSegment.from_file("../exo-dreams/The Veil Unfolds.mp3", format="mp3")
audio = audio.set_channels(1)  # mono
audio = audio.set_frame_rate(44100)
wav_path = "temp_audio.wav"
audio.export(wav_path, format="wav")

# Read the WAV file
rate, data = wav.read(wav_path)

# Downsample the waveform for visualization purposes
factor = int(len(data) / 5000)
data_ds = data[::factor]

# Simulate 9-dimensional weaving (project to 3D space, with phase shifts)
t = np.linspace(0, 1, len(data_ds))
x = data_ds * np.sin(2 * np.pi * t)
y = data_ds * np.cos(2 * np.pi * t)
z = data_ds * np.sin(4 * np.pi * t)

# Create a 3D projection to represent 9D weave
fig = plt.figure(figsize=(12, 6))
ax = fig.add_subplot(111, projection='3d')
ax.plot(x, y, z, linewidth=0.5)
ax.set_title("The Veil Unfolds — 9D Weave Projection")
ax.set_axis_off()

# Save and show
image_path = "veil_unfolds_9d_weave.png"
plt.savefig(image_path, bbox_inches='tight')
plt.close()

image_path
