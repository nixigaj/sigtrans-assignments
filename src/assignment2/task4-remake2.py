import numpy as np
import matplotlib.pyplot as plt

# Define parameters
period = 0.005  # Signal period
omega0 = 2 * np.pi / period  # Fundamental angular frequency
alpha = 1000 * np.pi  # System parameter
T = 0.015  # Time interval (15 ms)


# Create time vector
t = np.linspace(0, T, 1000)  # 1000 points in the interval [0, 15ms]

# Function to calculate y(t) for a given N


def calculate_output(N):
    n = np.arange(-N, N + 1)  # Range of harmonics
    n = n[n != 0]  # Exclude zero to avoid division by zero
    omega = n * omega0  # Angular frequencies

    # Fourier coefficients
    cn = np.exp(1J * np.pi * n) * 1j * (1 / (n * np.pi))

    # Transfer function
    H_omega = (alpha**2) / ((-omega**2) +
                            (2 * alpha * 1J * omega) + (alpha**2))
    X_omega = 2 * np.pi * cn

    # Compute the output spectrum Y(omega)
    Y_omega = H_omega * X_omega

    # Reconstruct y(t) using inverse Fourier transform
    y_t = np.zeros_like(t, dtype=complex)
    for i, time in enumerate(t):
        y_t[i] = np.sum(Y_omega * np.exp(1J * omega * time))

    # Divide by 2π as per the inverse Fourier transform
    return np.real(y_t) / (2 * np.pi)


# Calculate and plot y(t) for N = 1, 2, 10, 20
N_values = [1, 2, 10, 20]
plt.figure(figsize=(10, 8))

for i, N in enumerate(N_values, 1):
    y_t = calculate_output(N)
    plt.subplot(2, 2, i)
    # Convert t to ms for better visualization
    plt.plot(t * 1000, y_t, label=f"N = {N}")
    plt.title(f"Synthesized Signal for N = {N}")
    plt.xlabel("Time (ms)")
    plt.ylabel("y(t)")
    plt.grid()
    plt.legend()

# Adjust layout and show the plots
plt.tight_layout()
plt.show()