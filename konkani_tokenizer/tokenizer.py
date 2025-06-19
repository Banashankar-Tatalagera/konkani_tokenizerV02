import sentencepiece as spm
import os

class KonkaniTokenizer:
    def __init__(self):
        model_path = os.path.join(os.path.dirname(__file__), "spm_konkani.model")
        self.sp = spm.SentencePieceProcessor(model_file=model_path)

    def tokenize(self, text):
        return self.sp.encode(text, out_type=str)

    def encode(self, text):
        return self.sp.encode(text, out_type=int)

    def decode(self, ids):
        return self.sp.decode(ids)
