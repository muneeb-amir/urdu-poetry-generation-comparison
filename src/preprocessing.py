import re

def clean_text(text):
    text = re.sub(r"\s+", " ", text)
    text = text.strip()
    return text


def extract_lines(dataset):
    lines = []
    for item in dataset:
        poem = item["content"]
        lines.extend(poem.split("\n"))
    return [l for l in lines if len(l) > 2]