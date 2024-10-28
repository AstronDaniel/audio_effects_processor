# Digital Audio Effects Processor
## Project Overview
The Digital Audio Effects Processor is a Python application designed to apply audio effects like reverb, echo, and modulation to audio signals. Using Fourier Transform techniques and other digital signal processing (DSP) methods, this project allows users to explore and modify audio in real-time or offline. The project serves as a practical learning experience in audio processing and signal transformation.

## Features
- Reverb: Adds reverberation to audio, simulating an environment's acoustic characteristics.
- Echo: Introduces delayed repetition of the audio signal for an echo effect.
- Modulation: Alters audio parameters, allowing effects like vibrato or tremolo.

## Learning Goals
- Apply Fourier Transform techniques to convert audio signals between time and frequency domains.
- Use convolution in the frequency domain to add effects like reverb.
- Understand time-domain manipulations and how they relate to audio processing and synthesis.

## Project Structure
- `/main.py`: Entry point for the application.
- `/modules/`: Contains individual effect modules (reverb, echo, modulation).
- `/docs/`: Project documentation and reports.
- `/tests/`: Test cases for effects and core features.
- `/resources/`: Sample audio files for testing.

## Installation
### Prerequisites
- Python 3.x
- Required Libraries: `numpy`, `scipy`, `pyaudio`, `matplotlib` (optional for visualization)
### Steps
1. ##### Clone the Repository:

``` bash

git clone https://github.com/your-repository/audio-effects-processor.git
cd audio-effects-processor 
```
2. ##### Install Dependencies:

```bash

pip install -r requirements.txt
```
## Usage
1. ##### Run the Application:

```bash

python main.py
```
2. ##### Select an Effect:
- Choose the desired audio effect (reverb, echo, modulation) in the app.
- Adjust effect parameters to explore how each effect modifies the audio.
3. ##### Play and Save:
- Listen to the modified audio and, if desired, save it to a file.
