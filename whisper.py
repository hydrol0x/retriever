import numpy as np
import os
import openai
from scipy.io import wavfile
from audioin import record_audio
from pathlib import Path

# Get env variables
from dotenv import load_dotenv
load_dotenv()

def write_audio_to_file(full_audio: np.ndarray, filename: str, fs: int=44100) :
    # Scale the audio data to the range of int16, which is the format used for WAV files
    scaled_audio = np.int16(full_audio / np.max(np.abs(full_audio)) * 32767)
    
    # Write the audio data to a WAV file
    wavfile.write(filename, fs, scaled_audio)

def call_whisper_api(audio_stream: np.ndarray) -> None:
   # Call api on audio file path provided
    write_audio_to_file(audio_stream, r'./prompt.wav')
    openai.api_key = os.getenv("OPENAI_API_KEY")
    audio_file= open(r"./prompt.wav", "rb")
    transcript = openai.Audio.transcribe("whisper-1", audio_file)
    return transcript

def transcribe_mic_input():
    audio = record_audio()
    transcript = call_whisper_api(audio_stream=audio)
    print(f"audio transcript: {transcript}")
    return transcript
if __name__ == "__main__":
    audio = record_audio()
    transcript = call_whisper_api(audio_stream=audio)
    print(transcript)