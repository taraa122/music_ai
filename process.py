import os
import numpy as np
import librosa
import soundfile as sf

# Configuration
RAW_DATA_PATH = 'data/raw/'  # Path where your MP3 files are stored
PROCESSED_DATA_PATH = 'data/npy/'  # Path to save processed files
SEQ_LENGTH = 100  # Length of each sequence
SR = 22050  # Sample rate

def process_audio(file_path):
    """
    Process a single audio file and extract features.
    
    :param file_path: Path to the audio file.
    :return: Array of features.
    """
    print(f"Processing file: {file_path}")
    
    # Load the audio file
    audio_data, sample_rate = librosa.load(file_path, sr=SR)
    
    # Normalize audio data
    audio_data = audio_data / np.max(np.abs(audio_data))
    
    # Extract features (e.g., MFCCs, spectrograms)
    mfccs = librosa.feature.mfcc(y=audio_data, sr=sample_rate, n_mfcc=13)
    
    # Normalize features
    mfccs = (mfccs - np.mean(mfccs)) / np.std(mfccs)
    
    return mfccs

def preprocess_data(raw_data_path, processed_data_path, seq_length):
    """
    Preprocess all audio files in the raw data directory.
    
    :param raw_data_path: Directory containing raw audio files.
    :param processed_data_path: Directory to save preprocessed data.
    :param seq_length: Length of each sequence.
    """
    if not os.path.exists(processed_data_path):
        os.makedirs(processed_data_path)
        print(f"Created directory: {processed_data_path}")
    
    files_processed = 0
    
    for filename in os.listdir(raw_data_path):
        if filename.endswith('.mp3'):  # Process MP3 files
            file_path = os.path.join(raw_data_path, filename)
            features = process_audio(file_path)
            
            # Segment features into sequences
            num_segments = (features.shape[1] // seq_length) * seq_length
            sequences = features[:, :num_segments].reshape(-1, seq_length, features.shape[0])
            
            # Save sequences as .npy files
            np.save(os.path.join(processed_data_path, f"{os.path.splitext(filename)[0]}.npy"), sequences)
            print(f"Processed and saved {filename}")
            files_processed += 1
    
    if files_processed == 0:
        print("No files were processed. Ensure that the directory contains '.mp3' files.")
    else:
        print(f"Total files processed: {files_processed}")

if __name__ == '__main__':
    preprocess_data(RAW_DATA_PATH, PROCESSED_DATA_PATH, SEQ_LENGTH)
