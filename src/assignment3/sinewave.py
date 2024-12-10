import numpy as np
import matplotlib.pyplot as plt

# Parameters
duration = 0.01  # 10 ms for visualization
frequency = 1000  # Signal frequency (1 kHz)
f_s_high = 10000  # High sampling frequency (10 kHz)
f_s_low = 2000    # Lower-bound sampling frequency (2 kHz)

# Generate the continuous sine signal
# High-resolution time for continuous signal
t_cont = np.linspace(0, duration, 1000)
y_cont = np.sin(2 * np.pi * frequency * t_cont)

# Generate sampled sine signals
t_high = np.arange(0, duration, 1 / f_s_high)
y_high = np.sin(2 * np.pi * frequency * t_high)

t_low = np.arange(0, duration, 1 / f_s_low)
y_low = np.sin(2 * np.pi * frequency * t_low)

# Plot the signals
plt.figure(figsize=(8, 3))

# Continuous sine signal
plt.plot(t_cont, y_cont,
         color="red", linewidth=2, label="sin(2000πt)")

# Sine samples at 2 kHz
plt.stem(t_low, y_low, linefmt="blue", basefmt=" ",
         label="2kHz samples")


plt.xlabel("Time (s)", fontsize=12)
plt.ylabel("Amplitude", fontsize=12)
# Place legend in the top-right corner
plt.legend(loc='upper right', fontsize=12)

plt.grid(True)
plt.tight_layout()

# Show plot
plt.show()
