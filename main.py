from src.utils.constants import (
    example_text_01,
    example_text_02,
    example_text_03,
)
from src.tokenization.tokenize import Tokenizer
from src.normalization.normalize import Normalizer
from src.stop_words.stop_words_handler import StopWords
from src.stemming.stem import PorterStemming


def main():
    text_to_process = example_text_03
    print(f"Original text: {text_to_process}\n")

    normalizer = Normalizer(text_to_process)
    normalized_text = normalizer.normalization()
    print(f"Normalized text: {normalized_text}\n")

    tokenizer = Tokenizer(normalized_text)
    tokens = tokenizer.tokenize()
    print(f"Tokenized text: {tokens}")
    tokenizer.count_tokens()

    stop_words_remover = StopWords(normalized_text)
    text_without_stop_words = stop_words_remover.stop_word_removal()
    print(f"Text without stop words: {text_without_stop_words}\n")

    stemmer = PorterStemming(text_to_process)
    m_measurement_sequences = stemmer.m_measurement()
    print(f"M Measurement Sequences: {m_measurement_sequences}")


if __name__ == "__main__":
    main()
