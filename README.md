# Urdu Poetry Generation using RNN, LSTM, and Transformer

A comparative NLP project evaluating sequence-to-sequence models and optimizers for Urdu poetry generation.

---

## Overview

This project compares:

- RNN
- LSTM
- Transformer

with:

- Adam
- RMSprop
- SGD

Total: 9 model-optimizer combinations.

---

## Dataset

- Source: HuggingFace Urdu Poetry Dataset
- Total poems: ~1300
- Vocabulary size: ~10,500
- Sequence length: 20

---

## Results Summary

| Model | Optimizer | Perplexity |
|------|----------|-----------|
| RNN  | RMSprop  | **139.01 (Best)** |
| RNN  | Adam     | 193.13 |
| LSTM | RMSprop  | 198.68 |
| Transformer | Adam | 354.42 |

RNN + RMSprop performed best due to small dataset size.

---

## Key Insights

- Simpler models outperform complex ones on small datasets
- RMSprop works best for sequence modeling
- Transformers require larger datasets

---

## Project Structure

```
notebooks/
src/
results/
```

---

## Installation

```bash
pip install -r requirements.txt
```

---

## Run

Train models:
```bash
python src/train.py
```

Generate text:
```bash
python src/generate.py
```

---

## Features

- Full preprocessing pipeline
- 9 model-optimizer experiments
- Hyperparameter tuning
- Text generation with temperature control
- Quantitative + qualitative evaluation