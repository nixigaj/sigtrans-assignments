import numpy as np
import matplotlib.pyplot as plt

period = 0.005

N = 12

# range of n and exclude zero
n = np.arange(-N, N + 1)
n = n[n != 0]
omega = n * (2 * np.pi / period)

cn = np.exp(1J * np.pi * n) * (1j / (n * np.pi))
X_omega = 2 * np.pi * cn

# magnitude and phase
mag = np.abs(X_omega)
phase = np.angle(X_omega)

# wrapping
phase[n < 0] += 2 * np.pi
phase[n > 0] -= 2 * np.pi

plt.figure(figsize=(10, 3))

plt.subplot(1, 2, 1)
plt.stem(omega, mag, basefmt=" ")
plt.title("Magnitude of Fourier Coefficients")
plt.xlabel("Frequency (rad/s)")
plt.ylabel("Magnitude")
plt.grid()

# Phase plot
plt.subplot(1, 2, 2)
plt.stem(omega, phase, basefmt=" ")
plt.title("Phase of Fourier Coefficients")
plt.xlabel("Frequency (rad/s)")
plt.ylabel("Phase (radians)")
plt.grid()

# Show plots
plt.tight_layout()
plt.show()
