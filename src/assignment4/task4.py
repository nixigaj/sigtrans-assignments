import matplotlib.pyplot as plt
import numpy as np
from scipy.fft import fft

# Task 1: Theoretical Spectra
f1 = 21
f2 = 22  # f1 and f2
magnitude = 1/2  # Magnitude of the spectrum

# Task 2: Discrete Signals and DFT
fs = 128  # Sampling frequency in Hz
K = 128 # Number of samples
k = np.arange(0, K)  # Discrete-time indices

# Discrete signals
x1 = np.cos(2 * np.pi * f1 / fs * k)#
x2 = np.cos(2 * np.pi * f2 / fs * k)
x3 = x1 + x2

# Compute DFT for K = 20 points
X3 = fft(x3)  # Normalize by K
#X2 = fft(x2)

# Frequency bins
L = K
fl = np.arange(0, L) / L * fs  # Frequencies in Hz

X3_fl = np.abs(X3 * 1/K)
#X2_fl = np.abs(X2 * 1/K)

# Compute DFT for L = 256 points (zero-padding)
X3_zp = fft(x3)  # DFT with zero-padding to length 256
#X2_zp = fft(x2, n=256)

# Frequency bins for zero-padded spectra
L_zero_pad = 256
fl_zero_pad = np.arange(0, L_zero_pad) / L_zero_pad * fs  # Frequencies in Hz

X3_zp_fl = np.abs(X3_zp * 1/K)
#X2_zp_fl = np.abs(X2_zp * 1/K)



# Plot both theoretical and DFT-based spectra
plt.figure(figsize=(8, 4))


# Task 2: DFT-based spectra for K = 20
plt.stem(fl, X3_fl, label="|$X_3(f_l)$| (DFT, K=128)",
         basefmt=" ", linefmt='blue', markerfmt='bo')

# plt.stem(fl, X2_fl, label="", basefmt=" ", linefmt='green', markerfmt='go')

# Zero-padded DFT spectra for L = 256
#plt.stem(fl_zero_pad, X1_zp_fl, label="|$X_1(f_l)$| (DFT, L=256)", basefmt=" ", linefmt='green', markerfmt='go')
#plt.stem(fl_zero_pad, X2_zp_fl, label="|$X_2(f_l)$| (DFT, L=256)", basefmt=" ", linefmt='blue', markerfmt='bo')

# Task 1: Theoretical spectra
#plt.stem(f1, [magnitude], basefmt=" ", linefmt='b-', markerfmt='ro', label=f'|$X_1(f)$| (f = {f1} Hz)')
#plt.stem(f2, [magnitude], basefmt=" ", linefmt='b-', markerfmt='ro', label=f'|$X_2(f)$| (f = {f2} Hz)')

# Adjusting the x-axis ticks for more density
plt.xticks(np.arange(0, 65, 4))  # Set major ticks every 8 Hz
plt.xticks(np.arange(0, 65, 1), minor=True)  # Set minor ticks every 2 Hz

plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.xlim(0, 64)  # Frequency range 0 Hz to 64 Hz

plt.grid(True)
plt.legend(loc='upper right')

# Show the plot
plt.show()
