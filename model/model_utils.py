import librosa
import numpy as np
from tensorflow.keras.models import load_model

MODEL_SAVE_PATH = 'path_to_your_model.h5'

def load_model_from_file():
    """
    Load the model from the .h5 file.
    """
    model = load_model(MODEL_SAVE_PATH)
    return model

def extract_features(audio_file):
    """
    Extract features from a .wav file for prediction.
    """
    audio_data, sample_rate = librosa.load(audio_file, sr=None)
    features = librosa.feature.mfcc(y=audio_data, sr=sample_rate, n_mfcc=13)
    features = features.T
    return features

def predict_with_model(audio_file):
    """
    Predict using the loaded model and extracted features.
    """
    model = load_model_from_file()
    features = extract_features(audio_file)
    predictions = model.predict(features)
    return predictions
