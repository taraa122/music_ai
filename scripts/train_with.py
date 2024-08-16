import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM, TimeDistributed
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.utils import Sequence
import os

# Configuration
DATA_PATH = 'data/npy/'  # Updated data path
MODEL_SAVE_PATH = 'model/music_model.h5'
BATCH_SIZE = 32  # Reduced batch size
EPOCHS = 10
SEQ_LENGTH = 100  # Length of input sequences
VOCAB_SIZE = 256  # Number of unique tokens (e.g., MIDI notes, audio features)

class DataGenerator(Sequence):
    def __init__(self, data_path, batch_size, seq_length, vocab_size):
        self.data_path = data_path
        self.batch_size = batch_size
        self.seq_length = seq_length
        self.vocab_size = vocab_size
        self.files = [f for f in os.listdir(data_path) if f.endswith('.npy')]
        self.indexes = np.arange(len(self.files))
        
    def __len__(self):
        return int(np.ceil(len(self.files) / self.batch_size))
    
    def __getitem__(self, index):
        batch_files = self.files[index * self.batch_size:(index + 1) * self.batch_size]
        X_batch = []
        y_batch = []
        for file_name in batch_files:
            data = np.load(os.path.join(self.data_path, file_name))
            if data.ndim == 3:
                X_batch.append(data[:, :-1, :])
                y_batch.append(data[:, 1:, :])
                
        X_batch = np.concatenate(X_batch, axis=0)
        y_batch = np.concatenate(y_batch, axis=0)
        
        # Convert targets to integer encoding
        y_batch = np.argmax(y_batch, axis=-1)
        
        return X_batch, y_batch

def build_model(input_shape, vocab_size):
    model = Sequential()
    model.add(LSTM(128, return_sequences=True, input_shape=input_shape))
    model.add(LSTM(128, return_sequences=True))
    model.add(TimeDistributed(Dense(vocab_size, activation='softmax')))
    
    model.compile(loss='sparse_categorical_crossentropy', optimizer=Adam(), metrics=['accuracy'])
    
    return model

def train_model():
    """
    Train the music generation model.
    """
    # Create data generator
    train_generator = DataGenerator(DATA_PATH, BATCH_SIZE, SEQ_LENGTH, VOCAB_SIZE)
    
    # Build model
    model = build_model((SEQ_LENGTH, VOCAB_SIZE), VOCAB_SIZE)
    
    # Train model
    model.fit(train_generator, epochs=EPOCHS)
    
    # Save model
    model.save(MODEL_SAVE_PATH)
    print(f"Model saved to {MODEL_SAVE_PATH}")

if __name__ == '__main__':
    train_model()
