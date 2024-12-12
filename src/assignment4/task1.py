import matplotlib.pyplot as plt
import numpy as np

# Frequencies of the signals in Hz
frequencies_hz = [21, 22]  # f1 and f2
magnitude = 1/2  # Magnitude of the spectrum

# Create a figure for both plots
plt.figure(figsize=(10, 6))

# Plot |X1(f)| for f1 = 21 Hz
plt.stem([frequencies_hz[0]], [magnitude], basefmt=" ", 

         linefmt='b-', markerfmt='bo', label=f'|X1(f)| (f = {frequencies_hz[0]} Hz)')

# Plot |X2(f)| for f2 = 22 Hz
plt.stem([frequencies_hz[1]], [magnitude], basefmt=" ", 
         linefmt='r-', markerfmt='ro', label=f'|X2(f)| (f = {frequencies_hz[1]} Hz)')

# Add titles and labels
plt.title("Magnitude Spectra |X1(f)| and |X2(f)| (Scaled by π)")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude (π)")
plt.xlim(0, 64)  # Frequency range 0 Hz to 64 Hz
plt.ylim(0, 4)   # Magnitude range
plt.grid(True)
plt.legend()

# Show the plot
plt.show()
