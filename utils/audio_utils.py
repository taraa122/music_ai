import librosa
import soundfile as sf
import numpy as np

def process_audio(file_path):
    # Load the audio file
    audio_data, sample_rate = librosa.load(file_path, sr=None)
    
    # Normalize the audio data
    audio_data = audio_data / np.max(np.abs(audio_data))
    
    # Define the path for the processed audio
    processed_file_path = file_path.replace('.wav', '_processed.wav')
    
    # Save the processed audio
    sf.write(processed_file_path, audio_data, sample_rate)
    
    return processed_file_path

