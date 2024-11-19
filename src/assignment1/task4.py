import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import sounddevice as sd

start = 0.0
stop = 0.02

increment = 0.00001

t = np.arange(start, stop, increment)

x1 = np.sin(200 * np.pi * t)
x2 = np.sin(2000 * np.pi * t)
x3 = x1 + x2

alpha = 1000 * np.pi


def unit_step(t):
    return np.where(t >= 0, 1, 0)

u_t = unit_step(t)
h_t = np.pow(alpha, 2) * t * np.pow(np.e, -alpha * t) * u_t

y1 = increment * signal.convolve(x1, h_t, method="direct")
y2 = increment * signal.convolve(x2, h_t, method="direct")
y3 = increment * signal.convolve(x3, h_t, method="direct")

y1 = y1[0:int(0.02 / increment) + 1:1]
y1 = y1[0:t.shape[0]]

y2 = y2[0:int(0.02 / increment) + 1:1]
y2 = y2[0:t.shape[0]]

y3 = y3[0:int(0.02 / increment) + 1:1]
y3 = y3[0:t.shape[0]]

y1_y2 = y1 + y2

fig, bx = plt.subplots()
bx.plot(t, y3, label="y3(t)")
#bx.plot(t, y1_y2, label="y1(t)+y2(t)")
plt.legend()
plt.grid()
plt.show()

sd.play(y3, 1/increment, blocking=True)