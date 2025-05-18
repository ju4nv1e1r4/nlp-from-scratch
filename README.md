# NLP Text Processing Library

This Python project provides a simple implementation for performing basic Natural Language Processing (NLP) tasks on text data. It includes functionalities for:

- **Tokenization:** Breaking down text into individual words.
- **Stemming:** Reducing words to their root form.
- **Stop Word Removal:** Eliminating common words that don't carry significant meaning.
- **Normalization:** Converting text to a consistent format (lowercase).

## Project Structure

The project is organized as follows:

- `src/`: Contains the core Python code for the NLP functionalities.
    - `tokenization/tokenize.py`: Handles text tokenization.
    - `stemming/stem.py`: Implements stemming algorithms. (in progress...)
    - `stop_words/stop_words_handler.py`: Manages stop word removal.
    - `normalization/normalize.py`: Contains text normalization functions.
    - `utils/handler.py`: Utility functions.
    - `main.py`: Entry point or example usage.
- `constants.py`: Stores project-wide constants, including example text data.
- `requirements.txt`: Lists the project's dependencies.
- `README.md`: This file.