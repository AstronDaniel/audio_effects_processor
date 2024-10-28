# modules/echo.py

import numpy as np

def apply_echo(data, rate, delay=0.5, decay=0.6):
    """
    Applies an echo effect to the audio data.

    Parameters:
    - data: The original audio data.
    - rate: The sample rate of the audio.
    - delay: Delay time in seconds for the echo.
    - decay: Volume reduction factor for the echo.
    """
    # Convert delay time to samples
    delay_samples = int(rate * delay)
    
    # Check if data is multi-channel
    if len(data.shape) == 1:
        # Mono audio
        echo_data = np.copy(data)
        for i in range(delay_samples, len(data)):
            echo_data[i] += int(data[i - delay_samples] * decay)
    else:
        # Multi-channel audio
        echo_data = np.copy(data)
        for channel in range(data.shape[1]):
            for i in range(delay_samples, len(data)):
                echo_data[i, channel] += int(data[i - delay_samples, channel] * decay)
    
    # Ensure values are within allowed limits
    echo_data = np.clip(echo_data, -32768, 32767)  # For 16-bit PCM format
    return echo_data