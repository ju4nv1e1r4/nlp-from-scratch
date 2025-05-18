import re


class Handlers:
    def __init__(self, text: str):
        self.text = str(text) if text is not None else ""

    def remove_special_chars(self):
        pattern = re.compile(r"[^\w\s]")
        cleaned_text = pattern.sub("", self.text)
        return cleaned_text

    def remove_multiple_spaces(self):
        cleaned_text = re.sub(r'\s+', ' ', self.text).strip()
        return cleaned_text
