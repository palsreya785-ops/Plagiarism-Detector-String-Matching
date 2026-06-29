import re

class TextPreprocessor:

    def normalize(self, text):
        """
        Convert text to lowercase, remove punctuation,
        and remove extra spaces.
        """
        text = text.lower()

        text = re.sub(r'[^a-z0-9\s]', '', text)

        text = re.sub(r'\s+', ' ', text).strip()

        return text, None