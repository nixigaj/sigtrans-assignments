import numpy as np
import matplotlib.pyplot as plt

# Define parameters
period = 0.005

N = 75

# Create the range of n and exclude zero
n = np.arange(-N, N + 1)
n = n[n != 0]
omega = (n / period)

# Fourier coefficients
cn = np.exp(1J * np.pi * n) * 1j * (2 / (n))

# Transfer function
alpha = (1000 * np.pi)
H_omega = ((alpha)**2) /((-omega**2) + (2 * alpha * 1J * omega) + (alpha**2))

# Compute magnitude and phase
mag = (np.pi * np.abs(cn)) * np.abs(H_omega)
phase = (np.pi * np.angle(cn)) + np.angle(H_omega)

# Ensure phase stays within [-π, π]
phase[phase < -np.pi] += 2 * np.pi
phase[phase > np.pi] -= 2 * np.pi

# Plot magnitude and phase
plt.figure(figsize=(14, 6))

# Magnitude plot
plt.subplot(1, 2, 1)
plt.stem(omega, mag)
plt.title("Magnitude of Fourier Coefficients")
plt.xlabel("Frequency (rad/s)")
plt.ylabel("Magnitude")
plt.grid()

# Phase plot
plt.subplot(1, 2, 2)
plt.stem(omega, phase)
plt.title("Phase of Fourier Coefficients")
plt.xlabel("Frequency (rad/s)")
plt.ylabel("Phase (radians)")
plt.grid()

# Show plots
plt.tight_layout()
plt.show()
