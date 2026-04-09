import numpy as np

def generate_text(model, tokenizer, seed_text, max_len=20):
    for _ in range(max_len):
        token_list = tokenizer.texts_to_sequences([seed_text])[0]
        token_list = token_list[-max_len:]

        predicted = model.predict(np.array([token_list]), verbose=0)
        next_word = np.argmax(predicted)

        for word, index in tokenizer.word_index.items():
            if index == next_word:
                seed_text += " " + word
                break

    return seed_text