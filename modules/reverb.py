# modules/reverb.py

import numpy as np

def apply_reverb(data, rate, decay=0.5, num_delays=5, delay_time=0.02):
    """
    Applies a reverb effect to the audio data.

    Parameters:
    - data: The original audio data.
    - rate: The sample rate of the audio.
    - decay: The decay factor for each subsequent delay.
    - num_delays: The number of delayed signals to layer in the reverb.
    - delay_time: The time in seconds for each delay tap.
    """
    reverb_data = np.copy(data)

    if len(data.shape) == 1:
        # Mono audio
        for n in range(1, num_delays + 1):
            # Calculate delay in samples
            delay_samples = int(rate * delay_time * n)
            
            # Create decayed echo for each delay tap
            for i in range(delay_samples, len(data)):
                reverb_data[i] += int(data[i - delay_samples] * (decay ** n))
    else:
        # Multi-channel audio
        for channel in range(data.shape[1]):
            for n in range(1, num_delays + 1):
                # Calculate delay in samples
                delay_samples = int(rate * delay_time * n)
                
                # Create decayed echo for each delay tap
                for i in range(delay_samples, len(data)):
                    reverb_data[i, channel] += int(data[i - delay_samples, channel] * (decay ** n))
    
    # Ensure values are within allowed limits
    reverb_data = np.clip(reverb_data, -32768, 32767)  # For 16-bit PCM format
    return reverb_data