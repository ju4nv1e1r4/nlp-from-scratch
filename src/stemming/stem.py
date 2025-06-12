# WARNING: This file is not complete. 
# It's just a attempt to implement the Porter Stemmer algorithm.
# This implementation is in progress.

from ..tokenization.tokenize import Tokenizer

class M_measure:
    def __init__(self, word: str):
        self.word = word.lower()

    def is_vowel(self, char: str, index: int, word: str) -> bool:
        fixed_vowels = "aeiou"
        if char in fixed_vowels:
            return True
        elif char == "y" and index > 0 and not self.is_vowel(word[index - 1], index - 1, word):
            return True
        
        return False

    def measure(self) -> int:
        m_count = 0
        start_index = 0
        while start_index < len(self.word) and not self.is_vowel(self.word[start_index], start_index, self.word):
            start_index += 1
            
        if start_index >= len(self.word):
            return 0
        
        cv_sequence = []
        for i in range(start_index, len(self.word)):
            if self.is_vowel(self.word[i], i, self.word):
                cv_sequence.append('V')
            else:
                cv_sequence.append('C')

        cv_pattern = []
        if self.word:
            current_is_vowel = self.is_vowel(self.word[0], 0, self.word)
            cv_pattern.append('V' if current_is_vowel else 'C')

            for i in range(1, len(self.word)):
                is_vowel_char = self.is_vowel(self.word[i], i, self.word)
                if (is_vowel_char and cv_pattern[-1] == 'C') or (not is_vowel_char and cv_pattern[-1] == 'V'):
                    cv_pattern.append('V' if is_vowel_char else 'C')
        
        cv_string = "".join(cv_pattern)
        
        effective_cv_string = cv_string
        if effective_cv_string.startswith('C'):
            effective_cv_string = effective_cv_string[1:]

        if len(effective_cv_string) < 2:
            return 0
        
        count_m = 0
        is_in_vowel_region = False
        
        for i in range(start_index, len(self.word)):
            current_char_is_vowel = self.is_vowel(self.word[i], i, self.word)

            if current_char_is_vowel:
                is_in_vowel_region = True
            else:
                if is_in_vowel_region:
                    m_count += 1
                    is_in_vowel_region = False
        
        return m_count

class PorterStemming:
    def __init__(self, text: str):
        self.text = text
        self.tokenized_text = Tokenizer(self.text).tokenize()
            
    def stemmer(self) -> str:
        #TODO: implementar a lógica de porter stemming
        pass