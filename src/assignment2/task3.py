import numpy as np
import matplotlib.pyplot as plt

# Define parameters
period = 0.005

N = 12

# Create the range of n and exclude zero
n = np.arange(-N, N + 1)
n = n[n != 0]
omega = n * 2 * np.pi / period

# Fourier coefficients
cn = np.exp(1J * np.pi * n) * 1j * (1 / ((n) * np.pi))

# Transfer function
alpha = (1000 * np.pi)
H_omega = ((alpha)**2) /((-omega**2) + (2 * alpha * 1J * omega) + (alpha**2))
X_omega = 2 * np.pi * cn

# Compute magnitude and phase
mag = (np.abs(X_omega)) * np.abs(H_omega)
phase = (np.angle(X_omega)) + np.angle(H_omega)

# Ensure phase stays within [-π, π]
phase[phase < 0] += 2 * np.pi
phase[phase > 2 * np.pi] -= 2 * np.pi

# Plot magnitude and phase
plt.figure(figsize=(10, 3))

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
