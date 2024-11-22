import numpy as np
import matplotlib.pyplot as plt

# Constants
period = 0.005  # 5 ms
alpha = 1000 * np.pi
t = np.arange(0, 0.015, 0.00001)
omega_0 = (2 * np.pi) / period
N_vals = [1, 2, 10, 20]

# Initialize
y_t = np.zeros((4, t.size))
x_t = np.zeros((4, t.size))

k = 0

# Loop through different N values
for N in N_vals:
    n = np.arange(-N, N + 1)
    n = n[n != 0]  # Remove n=0 to avoid division by zero
    omega = n * (2 * np.pi) / period

    # Calculate X(w) and its magnitude and phase
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

    # Calculate H(w) and its magnitude and phase
    H_w = (alpha ** 2) / (-omega ** 2 + 2 * alpha * 1j * omega + alpha ** 2)
    H_mag = np.abs(H_w)
    H_phase = np.angle(H_w)

    # Compute Y(w)
    Y_mag = X_mag * H_mag
    Y_phase = X_phase + H_phase
    Y_w = Y_mag * np.exp(1j * Y_phase)

    # Define x(t)
    def xt(t):
        x = 0
        for i in range(len(n)):
            x += 1 / (2 * np.pi) * X_w[i] * np.exp(1j * n[i] * omega_0 * t)
        return np.real(x)

    # Define y(t)
    def yt(t):
        y = 0
        for i in range(len(n)):
            y += 1 / (2 * np.pi) * Y_w[i] * np.exp(1j * n[i] * omega_0 * t)
        return np.real(y)

    # Store results for plotting
    x_t[k] = xt(t)
    y_t[k] = yt(t)
    k += 1

# Plot results
plt.figure(figsize=(12, 6))

# Plot x(t) and y(t) on the same plot for each N
for i, N in enumerate(N_vals):
    plt.plot(t, y_t[i], label=f"y(t) for N={N}")
    plt.plot(t, x_t[i], label=f"x(t) for N={N}", alpha=0.3)

plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.legend()
plt.show()
