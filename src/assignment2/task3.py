import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import freqs

# Define parameters
period = 0.005
N = 12
n = np.arange(-N, N + 1)
n = n[n != 0]

#omega0 = (2 * np.pi / period)
omega = n * 2 * np.pi / period
alpha = 1000 * np.pi

X_w = np.exp(1j * np.pi * n) * 2j / n
X_mag = np.abs(X_w)
X_phase = np.angle(X_w)

for i in range(len(X_w)):
    if (i < N):
        if (X_phase[i] < 0):
            X_phase[i] += 2 * np.pi
    else:
        if (X_phase[i] >= 0):
            X_phase[i] -= 2 * np.pi


H_omega = (alpha**2) / (-(omega**2) + alpha * 2j * omega + alpha**2)
H_phase = np.angle(H_omega)

Y_mag = np.abs(X_w) * np.abs(H_omega)
Y_phase = X_phase + H_phase

plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
plt.stem(omega, X_mag, label="Input Magnitude")
plt.stem(omega, Y_mag, label="Output Magnitude", linefmt='r')
plt.title("Magnitude Spectrum of X(ω) and Y(ω)")
plt.xlabel("ω (rad/s)")
plt.ylabel("Magnitude")
plt.legend()
plt.grid()

x1, y1 = [0], [0]
plt.plot(x1, y1, marker='o')

x1, y1 = [0], [0]
plt.plot(x1, y1, marker='o', color='red')

plt.subplot(1, 2, 2)
plt.stem(omega, Y_phase, label="Output Phase", linefmt='r')
plt.stem(omega, X_phase, label="Input Phase")

plt.title("Phase Spectrum of X(ω) and Y(ω)")
plt.xlabel("ω (rad/s)")
plt.ylabel("Phase (radians)")
plt.legend()
plt.grid()

x1, y1 = [0], [0]
plt.plot(x1, y1, marker='o', color='red')

x1, y1 = [0], [0]
plt.plot(x1, y1, marker='o')

plt.tight_layout()
plt.show()
