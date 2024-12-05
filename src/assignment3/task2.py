import numpy as np
import sounddevice as sd

# Parameters
duration = 2 # seconds
Ts = 1/4000 # Sampling time (0.1 ms)
fs = 1 / Ts  # Sampling frequency (10 kHz)
frequency = 1000  # Signal frequency (Hz)

# Generate sampling points
t_k = np.arange(0, duration, Ts)

# Sample the signal
x_k = np.cos(2 * np.pi * frequency * t_k)

x_k2 = np.sin(2 * np.pi * frequency * t_k)

# Play the sampled signal
sd.play(x_k, fs, blocking=True)

sd.play(x_k2, fs, blocking=True)
