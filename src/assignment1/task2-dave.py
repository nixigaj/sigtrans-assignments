import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import sounddevice as sd

# Time increment
increment = 0.00001  # seconds

# Time vector ’t’
t = np.arange(0, 5, increment)

# Signal x1(t)
f1 = 1 / 0.01  # 100 Hz
x1 = np.sin(2 * np.pi * f1 * t)  # Amplitude 1, Phase shift 0

# Signal x2(t)
f2 = 1000  # 1000 Hz
x2 = np.sin(2 * np.pi * f2 * t)  # Amplitude 1, Phase shift 0

# Time vector ’t2’
t2 = np.arange(0, 0.005, increment)

alpha = 1000 * np.pi


def unit_step(t):
    return np.where(t >= 0, 1, 0)


u_t = unit_step(t2)
h_t = np.pow(alpha, 2) * t2 * np.pow(np.e, -alpha * t2) * u_t

# Approximation of the Dirac delta function
d = np.zeros(t2.shape)
d[0] = 1 / increment

y = increment * signal.convolve(d, h_t, method='direct')

y = y[0: int(0.02 / increment) + 1: 1]
y = y[0: t2.shape[0]]

# New figure bx
fig, bx = plt.subplots()
bx.plot(t2, h_t, label="h(t)")
bx.plot(t2, y, label="y(t)")
plt.legend()
plt.grid()
plt.show()