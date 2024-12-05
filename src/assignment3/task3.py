import numpy as np
import sounddevice as sd

# Parameters
duration = 10  # seconds
original_fs = 40000  # Original sampling frequency (40 kHz)
target_fs = 8000  # Target sampling frequency (8 kHz)

# Step 1: Record the signal
print("Recording for 10 seconds...")
K = int(duration * original_fs)  # Total number of samples
x = sd.rec(K, samplerate=original_fs, channels=1,
           dtype='float32', blocking=True)
print("Recording complete.")

# Step 2: Downsample the signal
x_downsampled = x[::5]  # Take every 5th sample

# Step 3: Play back the original recording
print("Playing original recording...")
sd.play(x, samplerate=original_fs, blocking=True)

# Step 4: Play back the downsampled recording
print("Playing downsampled recording...")
sd.play(x_downsampled, samplerate=target_fs, blocking=True)

# Step 5: Check the shape of the downsampled signal
print(f"Original recording shape: {x.shape}")
print(f"Downsampled recording shape: {x_downsampled.shape}")

# Inform the user
print("Playback complete. Compare the audio quality of the two recordings.")
