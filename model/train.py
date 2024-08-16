import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM, TimeDistributed
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.models import load_model
import sys
import os

print("Python Path:", sys.path)

try:
    from utils.audio_utils import process_audio
    print("Import successful!")
except ImportError as e:
    print(f"Import failed: {e}")

# Configuration
DATA_PATH = 'data/npy/'
MODEL_SAVE_PATH = 'model/music_model.h5'
BATCH_SIZE = 64
EPOCHS = 10
SEQ_LENGTH = 100  # Length of input sequences
VOCAB_SIZE = 256  # Number of unique tokens (e.g., MIDI notes, audio features)

def load_data(data_path):
    """
    Load and preprocess the music data.
    
    :param data_path: Path to the data directory.
    :return: Processed input sequences and targets.
    """
    sequences = []
    targets = []
    
    for filename in os.listdir(data_path):
        if filename.endswith('.npy'):
            data = np.load(os.path.join(data_path, filename))
            print(f"Loaded {filename} with shape {data.shape}")
            if data.ndim == 3:  # Ensure data is in the correct shape
                sequences.append(data[:, :-1, :])
                targets.append(data[:, 1:, :])  # Skip the first timestep for targets
                
    if not sequences:
        raise ValueError("No valid data found in the specified directory.")
    
    X = np.concatenate(sequences, axis=0)
    y = np.concatenate(targets, axis=0)
    
    # Convert targets to one-hot encoding
    y = to_categorical(y, num_classes=VOCAB_SIZE)
    
    print(f"Data shapes - X: {X.shape}, y: {y.shape}")
    
    return X, y

def build_model(input_shape, vocab_size):
    """
    Build and compile the music generation model.
    
    :param input_shape: Shape of the input data.
    :param vocab_size: Number of unique tokens (e.g., MIDI notes, audio features).
    :return: Compiled Keras model.
    """
    model = Sequential()
    model.add(LSTM(128, return_sequences=True, input_shape=input_shape))
    model.add(LSTM(128, return_sequences=True))
    model.add(TimeDistributed(Dense(vocab_size, activation='softmax')))
    
    model.compile(loss='categorical_crossentropy', optimizer=Adam(), metrics=['accuracy'])
    
    return model

def load_model_from_file():
    """
    Load the trained model from the file.
    
    :return: Loaded Keras model.
    """
    model = load_model(MODEL_SAVE_PATH)
    print(f"Model loaded from {MODEL_SAVE_PATH}")
    return model

def train_model():
    """
    Train the music generation model.
    """
    # Load data
    X, y = load_data(DATA_PATH)
    
    # Build model
    model = build_model((X.shape[1], X.shape[2]), VOCAB_SIZE)
    
    # Train model
    model.fit(X, y, batch_size=BATCH_SIZE, epochs=EPOCHS, validation_split=0.1)
    
    # Save model
    model.save(MODEL_SAVE_PATH)
    print(f"Model saved to {MODEL_SAVE_PATH}")

if __name__ == '__main__':
    train_model()
