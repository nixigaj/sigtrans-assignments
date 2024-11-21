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
cn = np.exp(1J * np.pi * n) * 1j * (1 / (n * np.pi))

# Transfer function
alpha = (1000 * np.pi)
H_omega = (alpha ** 2) / ((-omega ** 2) + (2 * alpha * 1J * omega) + (alpha ** 2))
X_omega = 2 * np.pi * cn

X_mag = np.abs(X_omega)

# Compute magnitude and phase
mag = (np.abs(X_omega)) * np.abs(H_omega)
phase = (np.angle(X_omega)) + np.angle(H_omega)

X_phase = np.angle(X_omega)
H_phase = np.angle(H_omega)

for i in range(len(X_omega)):
    if i < N:
        if X_phase[i] < 0:
            X_phase[i] += 2 * np.pi
    else:
        if X_phase[i] > 0:
            X_phase[i] -= 2 * np.pi

Y_phase = X_phase + H_phase



# Ensure phase stays within [-π, π]
#phase[phase < 0] += 2 * np.pi
#phase[phase > 2 * np.pi] -= 2 * np.pi

# Plot magnitude and phase
plt.figure(figsize=(10, 3))

# Magnitude plot
plt.subplot(1, 2, 1)
plt.stem(omega, X_mag)
plt.title("Magnitude of Fourier Coefficients")
plt.xlabel("Frequency (rad/s)")
plt.ylabel("Magnitude")
plt.grid()

# Add dot at zero
x1, y1 = [0], [0]
plt.plot(x1, y1, marker='o')

# Phase plot
plt.subplot(1, 2, 2)
plt.stem(omega, X_phase)
plt.title("Phase of Fourier Coefficients")
plt.xlabel("Frequency (rad/s)")
plt.ylabel("Phase (radians)")
plt.grid()

# Add dot at zero
x1, y1 = [0], [0]
plt.plot(x1, y1, marker='o')

# Show plots
plt.tight_layout()
plt.show()
