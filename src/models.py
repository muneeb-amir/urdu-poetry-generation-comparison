from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, SimpleRNN, LSTM, Dense

def build_rnn(vocab_size, seq_len):
    model = Sequential([
        Embedding(vocab_size, 128, input_length=seq_len),
        SimpleRNN(256),
        Dense(vocab_size, activation="softmax")
    ])
    return model


def build_lstm(vocab_size, seq_len):
    model = Sequential([
        Embedding(vocab_size, 128, input_length=seq_len),
        LSTM(256),
        Dense(vocab_size, activation="softmax")
    ])
    return model