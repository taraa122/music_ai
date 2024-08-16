import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences

def generate_music(model, start_sequence, vocab_size, sequence_length, temperature=1.0):
    """
    Generate a music sequence based on a starting sequence.

    :param model: Trained Keras model for music generation.
    :param start_sequence: Initial sequence to seed the generation.
    :param vocab_size: Size of the vocabulary (number of unique tokens).
    :param sequence_length: Length of the generated sequence.
    :param temperature: Sampling temperature for creativity (higher is more random).
    :return: Generated music sequence.
    """
    # Ensure the start sequence is the correct length
    input_sequence = pad_sequences([start_sequence], maxlen=sequence_length, truncating='pre')
    generated_sequence = list(start_sequence)

    for _ in range(sequence_length):
        # Make predictions
        predictions = model.predict(input_sequence)[0]

        # Apply temperature
        predictions = np.log(predictions + 1e-10) / temperature
        predictions = np.exp(predictions) / np.sum(np.exp(predictions))

        # Sample from predictions
        next_token = np.random.choice(range(vocab_size), p=predictions)

        # Update the sequence
        generated_sequence.append(next_token)
        input_sequence = pad_sequences([generated_sequence[-sequence_length:]], maxlen=sequence_length, truncating='pre')

    return generated_sequence

def load_model_from_file(model_path):
    """
    Load a model from a file.

    :param model_path: Path to the model file.
    :return: Loaded Keras model.
    """
    model = load_model(model_path)
    print(f"Model loaded from {model_path}")
    return model

def main():
    # Parameters (adjust these based on your project)
    model_path = 'music_model.h5'    # Path to the trained model
    vocab_size = 5000                # Vocabulary size
    sequence_length = 50            # Length of the input sequence
    start_sequence = [0] * sequence_length  # Example starting sequence (replace with actual tokens)
    temperature = 1.0                # Temperature for sampling

    # Load the trained model
    model = load_model_from_file(model_path)
    
    # Generate music
    generated_sequence = generate_music(model, start_sequence, vocab_size, sequence_length, temperature)
    
    # Print the generated sequence
    print("Generated music sequence:", generated_sequence)

if __name__ == "__main__":
    main()
