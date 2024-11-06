import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import sounddevice as sd

# The unit of time used is seconds

start = 0.0
stop = 5.0

increment = 0.00001

t = np.arange(start, stop, increment)

x1 = np.sin(200 * np.pi * t)
x2 = np.sin(2000 * np.pi * t)
x3 = x1 + x2

fig, ax = plt.subplots()
ax.plot(t, x1, label="x_1(t)")
ax.plot(t, x2, label="x_2(t)")
ax.plot(t, x3, label="x_3(t)")

ax.set_xlim(0, 0.01)
ax.set_xlabel("Time (s)")
ax.set_ylabel("Amplitude")

ax.legend()
plt.grid()
plt.show()

sd.play(x1, 1/increment, blocking=True)
sd.play(x2, 1/increment, blocking=True)
sd.play(x3, 1/increment, blocking=True)
