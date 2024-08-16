from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM

def create_model(input_shape):
    model = Sequential()
    model.add(LSTM(64, input_shape=input_shape, return_sequences=True))
    model.add(LSTM(64, return_sequences=False))
    model.add(Dense(1, activation='sigmoid'))
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return model

def load_model_from_file(model_path):
    from tensorflow.keras.models import load_model
    return load_model(model_path)

def save_model(model, model_path):
    model.save(model_path)

