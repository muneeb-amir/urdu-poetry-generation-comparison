from datasets import load_dataset

def load_poetry_dataset():
    dataset = load_dataset("ReySajju742/Urdu-Poetry-Dataset")
    return dataset["train"]