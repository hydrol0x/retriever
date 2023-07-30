import pyaudio
import numpy as np
from scipy.io import wavfile
import time

def record_audio(threshold=0.006, fs=44100, duration=2):
    # Initialize a buffer with duration 
    buffer = np.zeros((fs * duration,))
    audio_chunks = []  # List to store individual chunks of audio data

    # Create an instance of PyAudio
    p = pyaudio.PyAudio()

    # This callback function will be called by PyAudio to fill the buffer
    def callback(in_data, frame_count, time_info, status):
        audio_data = np.frombuffer(in_data, dtype=np.float32)
        buffer[:-frame_count] = buffer[frame_count:]
        buffer[-frame_count:] = audio_data
        audio_chunks.append(audio_data)  # Append the chunk to the list
        return (in_data, pyaudio.paContinue)

    # Open a new recording stream and start recording
    stream = p.open(format=pyaudio.paFloat32,
                    channels=1,
                    rate=fs,
                    input=True,
                    input_device_index=0,
                    stream_callback=callback)
    stream.start_stream()
    print(f"Recording audio...")

    count = 0  # sets a delay
    while stream.is_active():
        # Calculate the RMS of the buffer
        rms = np.sqrt(np.mean(buffer**2))
        
        # If the RMS is below the threshold and the , stop recording
        print(f"[INFO] RMS: {rms}")
        if count > 10 and rms < threshold:
            print("Running commands... TEST")
            break
        
        # Sleep for a while to reduce CPU usage
        time.sleep(0.1)
        count += 1

    # Stop the stream and close it
    stream.stop_stream()
    stream.close()
    
    # Terminate the PyAudio object
    p.terminate()

    # Convert the list of audio chunks into a single array
    full_audio = np.concatenate(audio_chunks)

    # Return the full recorded audio as well as the buffer
    return full_audio

