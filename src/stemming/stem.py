# WARNING: This file is not complete. 
# It's just a attempt to implement the Porter Stemmer algorithm.
# This implementation is in progress.

from ..tokenization.tokenize import Tokenizer


class PorterStemming:
    def __init__(self, text: str):
        self.text = text
        self.tokenized_text = Tokenizer(self.text).tokenize()

    def m_measurement(self) -> int:
        def verify_if_y_is_vowel(word: str) -> bool:
            vowels = ["a", "e", "i", "o", "u"]
            vowels_with_y = ["a", "e", "i", "o", "u", "y"]
            if word.startswith("y"):
                return True
            else:
                return False

        word = self.tokenized_text[2]
        print(word)
        status = verify_if_y_is_vowel(word)
        print(status)
        #TODO: implement complete m measurement algorithm

            
    def stemmer(self) -> str:
        tokenizer = Tokenizer(self.text)
        tokens = tokenizer.tokenize()

        stemmed_tokens = []
        for token in tokens:
            if token.endswith("ing"):
                stemmed_tokens.append(token[:-3])
            elif token.endswith("ed"):
                stemmed_tokens.append(token[:-2])
            else:
                stemmed_tokens.append(token)

        return " ".join(stemmed_tokens)
        #TODO: modify stem logic