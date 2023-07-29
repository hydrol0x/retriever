import numpy as np
import openai
from scipy.io import wavfile

# Get env variables
from dotenv import load_dotenv
load_dotenv()

def write_audio_to_file(full_audio: np.ndarray, filename: str, fs: int=44100) -> str:
    # Scale the audio data to the range of int16, which is the format used for WAV files
    scaled_audio = np.int16(full_audio / np.max(np.abs(full_audio)) * 32767)
    
    # Write the audio data to a WAV file
    wavfile.write(filename, fs, scaled_audio)
    return filename

def call_whisper_api(audio_stream: np.ndarray) -> None:
   # Call api on audio file path provided
    audio_file = write_audio_to_file(audio_stream, './prompt.wav')
    with open(audio_file, "rb") as f:
        transcript = openai.Audio.transcribe("whisper-1", audio_file)