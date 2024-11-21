import numpy as np
import matplotlib.pyplot as plt


period = 0.005  # 5 ms
alpha = 1000 * np.pi
t = np.arange(0, 0.015, 0.00001)
omega_0 = (2 * np.pi) / period

N_vals = [1, 2, 10, 20]
plt.figure(figsize=(10, 6))

k = 0
y_t = np.zeros((4, t.size))

for N in N_vals:
    n = np.arange(-N, N + 1)
    n = n[n != 0]
    omega = n * (2 * np.pi) / period

    X_w = np.exp(1j * np.pi * n) * 2j / n
    X_mag = np.abs(X_w)
    X_phase = np.angle(X_w)

    for i in range(len(X_w)):
        if i < N:
            if X_phase[i] < 0:
                X_phase[i] += 2 * np.pi
        else:
            if X_phase[i] > 0:
                X_phase[i] -= 2 * np.pi

    H_w = (alpha ** 2) / (-omega ** 2 + 2 * alpha * 1j * omega + alpha ** 2)
    H_mag = np.abs(H_w)
    H_phase = np.angle(H_w)

    Y_mag = X_mag * H_mag
    Y_phase = X_phase + H_phase
    Y_w = Y_mag * np.exp(1j * Y_phase)

    def yt(t):
        y = 0
        for i in range(len(n)):
            y += 1 / (2* np.pi) * Y_w[i] * np.exp(1j * n[i] * omega_0 * t)
        return np.real(y)

    y = yt(t)
    y_t[k] = y
    k += 1

plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude")
plt.plot(t, y_t[0], label="N=1")
plt.plot(t, y_t[1], label="N=2")
plt.plot(t, y_t[2], label="N=10")
plt.plot(t, y_t[3], label="N=20")

plt.legend()

#plt.plot(t, y_t[0], t,  y_t[1], t,  y_t[2], t, y_t[3])
plt.grid(True)
plt.show()
