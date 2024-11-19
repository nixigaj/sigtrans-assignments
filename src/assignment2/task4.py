import numpy as np
import matplotlib.pyplot as plt

# Define parameters
period = 0.005
omega0 = (2 * np.pi / period)
alpha = 1000 * np.pi
t = np.linspace(0, 15e-3, 1000)  # Time vector from 0 to 15 ms
N_values = [1, 2, 10, 20]  # Different values of N

# Define Fourier coefficients for x(t)
n = np.arange(-50, 51)
n = n[n != 0]  # Exclude n = 0
freqs = n * omega0
cn = np.exp(1J * np.pi * n) * 1j * (2 / n)

# Transfer function H(omega)
H_omega = (alpha**2) / ((-freqs**2) + (2 * alpha * 1j * freqs) + alpha**2)

# Calculate Y(omega)
Y_omega = cn * H_omega

# Plot y(t) for different values of N
plt.figure(figsize=(12, 8))

for i, N in enumerate(N_values):
    n_selected = np.arange(-N, N + 1)
    freqs_selected = n_selected * omega0
    Y_selected = Y_omega[np.isin(n, n_selected)]

    # Reconstruct y(t)
    y_t = np.zeros_like(t, dtype=complex)
    for k, Y_k in zip(n_selected, Y_selected):
        y_t += Y_k * np.exp(1j * k * omega0 * t)
    y_t = np.real(y_t)  # Remove residual imaginary parts

    # Plot
    plt.subplot(2, 2, i + 1)
    plt.plot(t * 1e3, y_t, label=f'N = {N}')
    plt.title(f'Reconstructed Signal y(t) for N = {N}')
    plt.xlabel('Time (ms)')
    plt.ylabel('Amplitude')
    plt.grid()
    plt.legend()

plt.tight_layout()
plt.show()
