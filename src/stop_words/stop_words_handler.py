from ..utils.handler import Handlers
from ..tokenization.tokenize import Tokenizer
from ..normalization.normalize import Normalizer


class StopWords:
    def __init__(self, text: str):
        self.text = text
        self.stop_words_list = {
            "a", "se", "in", "if",
            "of", "on", "the", "an",
            "and", "or", "at", "is",
            "at", "am", "are", "it",
            "he", "she", "they", "but",
            "than", "to", "its", "for"
        }

    def stop_word_removal(self) -> str:
        normalizer = Normalizer(self.text)
        normalized_text = normalizer.normalization()
        tokenizer = Tokenizer(normalized_text)
        without_stop_words = [word for word in tokenizer.tokenize() if word not in self.stop_words_list]
        text_without_stop_words = " ".join(without_stop_words)
        return text_without_stop_words
