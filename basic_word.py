# basic_word.py

class BasicWord:

    def __init__(self, original_word, subwords):

        self.original_word = original_word
        self.subwords = subwords

    def check_word(self, word):
        return word in self.subwords

    def count_subwords(self):
        return len(self.subwords)

    def __repr__(self):
        return f"Исходное слово: {self.original_word}, Подслова: {', '.join(self.subwords)}"
