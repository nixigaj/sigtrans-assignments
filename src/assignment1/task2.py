import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import sounddevice as sd

start = 0.0
stop = 0.02

increment = 0.00001

t = np.arange(start, stop, increment)

alpha = 1000 * np.pi

def unit_step(t):
    return np.where(t >= 0, 1, 0)
    
u_t = unit_step(t)
h_t = np.pow(alpha, 2) * t * np.pow(np.e, -alpha * t) * u_t

d = np.zeros(t.shape)
d[0] = 1 / increment

y = increment * signal.convolve(d, h_t, method="direct")

y = y[0:int(0.02/increment) + 1:1]
y = y[0:t.shape[0]]

fig, bx = plt.subplots()
bx.plot(t, h_t, label="h(t)")
bx.plot(t, y, label="y(t)")
plt.legend()
plt.grid()
plt.show()
