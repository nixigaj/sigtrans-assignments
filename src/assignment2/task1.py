import numpy as np
import matplotlib.pyplot as plt

# Define parameters
period = 0.005
omega = (2 * np.pi / period)
N = 50

# Create the range of n and exclude zero
n = np.arange(-N, N + 1)
n = n[n != 0]

# Frequency components
freqs = n * omega

# Fourier coefficients
cn = np.exp(1J * np.pi * n) * 1j * 2 / (np.pi * n)

# Compute magnitude and phase
mag = np.abs(cn)
phase = np.angle(cn)

# Ensure phase stays within [-π, π]
phase[phase < -np.pi] += 2 * np.pi
phase[phase > np.pi] -= 2 * np.pi

# Define the interval for frequencies
lower_bound = -15e3
upper_bound = 15e3

# Filter frequencies and coefficients within the interval
mask = (freqs >= lower_bound) & (freqs <= upper_bound)
filtered_freqs = freqs[mask]
filtered_mag = mag[mask]
filtered_phase = phase[mask]

# Plot magnitude and phase
plt.figure(figsize=(14, 6))

# Magnitude plot
plt.subplot(1, 2, 1)
plt.stem(filtered_freqs, filtered_mag, basefmt=" ")
plt.title("Magnitude of Fourier Coefficients")
plt.xlabel("Frequency (rad/s)")
plt.ylabel("Magnitude")
plt.grid()

# Phase plot
plt.subplot(1, 2, 2)
plt.stem(filtered_freqs, filtered_phase, basefmt=" ")
plt.title("Phase of Fourier Coefficients")
plt.xlabel("Frequency (rad/s)")
plt.ylabel("Phase (radians)")
plt.grid()

# Show plots
plt.tight_layout()
plt.show()
