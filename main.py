import os
import scipy.io.wavfile as wav
import numpy as np
import warnings
import pyaudio
from scipy.io.wavfile import WavFileWarning
from modules.echo import apply_echo

# Suppress the WavFileWarning
warnings.simplefilter("ignore", WavFileWarning)

# Function to load audio
def load_audio(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    rate, data = wav.read(file_path)
    return rate, data

# Function to play audio
def play_audio(rate, data):

    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16, channels=1, rate=rate, output=True)
    stream.write(data.tobytes())
    stream.close()
    p.terminate()

# Function to save modified audio
def save_audio(file_path, rate, data):
    wav.write(file_path, rate, data.astype(np.int16))

# Test functions
if __name__ == "__main__":
    # Load audio
    rate, data = load_audio("tests/test.wav")
    
    # Apply the echo effect from the echo module
    data_with_echo = apply_echo(data, rate, delay=0.5, decay=0.6)
    
   
    # Save the output
    save_audio("tests/output/output_with_echo.wav", rate, data_with_echo)

    # Play the output audio
    play_audio(rate, data_with_echo)