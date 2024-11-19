import numpy as np
import matplotlib.pyplot as plt

# Define alpha and frequency range
alpha = 1000 * np.pi
omega_range = np.linspace(-15e3, 15e3, 1000)  # Dense grid of frequencies

# Calculate H(jω) for each frequency
H_omega = (alpha ** 2) / (-omega_range ** 2 + 1j * 2 * alpha * omega_range + alpha ** 2)

# Magnitude and phase of H(jω)
magnitude = np.abs(H_omega)
phase = np.angle(H_omega)

# Plotting the magnitude and phase response
plt.figure(figsize=(14, 6))

# Magnitude plot
plt.subplot(1, 2, 1)
plt.plot(omega_range, magnitude)
plt.title("Magnitude of Frequency Response")
plt.xlabel(r"$\omega$ (rad/s)")
plt.ylabel("Magnitude")
plt.grid()

# Phase plot
plt.subplot(1, 2, 2)
plt.plot(omega_range, phase)
plt.title("Phase of Frequency Response")
plt.xlabel(r"$\omega$ (rad/s)")
plt.ylabel("Phase (radians)")
plt.grid()

# Show plots
plt.tight_layout()
plt.show()
