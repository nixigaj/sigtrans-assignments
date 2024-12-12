import numpy as np
import matplotlib.pyplot as plt

# Parameters
fs = 128  # Sampling frequency in Hz
f1, f2 = 21, 22  # Natural frequencies in Hz
K = 20  # Number of samples
k = np.arange(0, K)  # Discrete-time indices
t = np.linspace(0, K/fs, 500)  # Continuous time for smooth cosine waves

# Signals
x1_discrete = np.cos(2 * np.pi * f1 / fs * k)  # Discrete-time x1
x2_discrete = np.cos(2 * np.pi * f2 / fs * k)  # Discrete-time x2
x1_continuous = np.cos(2 * np.pi * f1 * t)  # Continuous-time x1
x2_continuous = np.cos(2 * np.pi * f2 * t)  # Continuous-time x2

# Plot
fig, ax = plt.subplots(figsize=(8, 4))

# Plot continuous signals
ax.plot(t * fs, x1_continuous, 'b-',
        label='$x_1(t)$')
ax.plot(t * fs, x2_continuous, 'r-',
        label='$x_2(t)$')

# Plot discrete-time signals with stems
ax.stem(k, x1_discrete, linefmt='b--', markerfmt='bo', basefmt='k-',
        label='$x_1[k]$')
ax.stem(k, x2_discrete, linefmt='r--', markerfmt='ro', basefmt='k-',
        label='$x_2[k]$')

# Styling the plot
ax.set_title('Comparison of Continuous and Discrete-Time Signals', fontsize=14)
ax.set_xlabel('Discrete-time variable $k$', fontsize=12)
ax.set_ylabel('Amplitude', fontsize=12)
plt.legend(loc='upper right', fontsize=12)
ax.grid(True)
ax.set_xticks(np.arange(0, K))  # Set x-ticks to every integer step


plt.show()
