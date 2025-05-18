from ..tokenization.tokenize import Tokenizer
from ..utils.handler import Handlers


class Normalizer:
    def __init__(self, text: str):
        self.text = text

    def normalization(self) -> str:
        handler = Handlers(self.text)
        self.text = handler.remove_special_chars()
        normalized_text = self.text.lower()
        return normalized_text
