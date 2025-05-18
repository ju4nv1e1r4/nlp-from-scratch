from ..utils.handler import Handlers


class Tokenizer:
    def __init__(self, text: str):
        self.text = text

    def tokenize(self) -> list:
        handler = Handlers(self.text)
        processed_text = handler.remove_special_chars()
        processed_text = Handlers(processed_text).remove_multiple_spaces()
        if not processed_text:
            return []

        tokens = processed_text.split()
        return tokens

    def count_tokens(self) -> int:
        tokens = self.tokenize()
        print(f"Número de tokens: {len(tokens)}")
        return len(tokens)