# Konkani Tokenizer

A custom tokenizer built using SentencePiece for Automatic Speech Recognition (ASR) fine-tuning in the Konkani language. This tokenizer is trained on a curated dataset consisting of Konkani textbooks and transcribed audio, optimized for use with LLMs and speech models.

## 🚀 Features

- SentencePiece-based tokenizer
- Designed specifically for Konkani language
- Compatible with ASR fine-tuning workflows
- Trained on real-world textbook and audio transcript data

## 🛠 Installation & Usage

```bash
pip install git+https://github.com/Banashankar-Tatalagera/konkani_tokenizerV02.git
```


📦 Dependencies

    tokenizers

    sentencepiece






## for testing the tokenizer
### save this code in the jupyterNOtebook or .py file and run:

```bash
from konkani_tokenizer import KonkaniTokenizer

tokenizer = KonkaniTokenizer()

text = "हांव कालेर मोरगांव गेलो आंव भितर थोडे वेळाचेर मितरांक सोबत उबोंट आनी चाय घेतलो, तांचे संगत मजेचेर आसा."
tokens = tokenizer.tokenize(text)
ids = tokenizer.encode(text)
decoded = tokenizer.decode(ids)

print("Tokens:", tokens)
print("Token IDs:", ids)
print("Decoded Text:", decoded)

```