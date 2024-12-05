import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import sounddevice as sd

# Parameters for the filter
order = 4              # Filter order
cutoff_freq = 3400     # Cut-off frequency in Hz (3.4 kHz)
original_fs = 40000   # Original recording frequency (40 kHz)
new_sampling_freq = 8000  # New sampling frequency (8 kHz)
duration = 10         # Duration of the recording in seconds

# Step 1: Record the signal
print("Recording for 10 seconds...")
K = int(duration * original_fs)  # Total number of samples
x = sd.rec(K, samplerate=original_fs, channels=1,
           dtype='float32', blocking=True)
print("Recording complete.")

# 1. Design the 4th order Butterworth filter (analog)
wn = 2 * np.pi * cutoff_freq  # Cut-off frequency in rad/s
z, p, k = signal.butter(order, wn, analog=True, output='zpk')

# 2. Create the transfer function
H = signal.ZerosPolesGain(z, p, k)

# 3. Calculate and plot the frequency response
w, magnitude, phase = signal.bode(H, n=1000)

# Convert angular frequency to Hz and magnitude from dB to gain
frequencies = w / (2 * np.pi)  # Convert from rad/s to Hz
magnitude_linear = 10 ** (magnitude / 20)  # Convert dB to linear scale

# Plot the magnitude response
plt.figure(figsize=(6, 4))
plt.plot(frequencies, magnitude_linear)
plt.xlabel("Frequency (Hz)", fontsize=12)
plt.ylabel("Gain", fontsize=12)
plt.grid(True, which='both')
plt.xlim([1000, 10000])  # Frequency range from 1 kHz to 10 kHz
plt.tight_layout()
plt.show()

# 4. Apply the filter to the recorded signal using the transfer function
time = np.linspace(0, duration, K)  # Time vector for the signal
# Apply filter to the recorded signal
t_filtered, x_filtered, _ = signal.lsim(H, x.flatten(), time)

# 5. Resample the filtered signal
# Downsample by selecting every 5th sample for 8 kHz sampling rate
x_resampled = x_filtered[::5]

# 6. Play the resampled signal
sd.play(x_resampled, new_sampling_freq, blocking=True)
