# players.py

class Player:

    def __init__(self, username):
        self.username = username
        self.used_words = []

    def get_used_word_count(self):

        return len(self.used_words)

    def add_used_word(self, word):

        self.used_words.append(word)

    def is_word_used(self, word):

        return word in self.used_words

    def __repr__(self):

        return f"Игрок: {self.username}, Использованные слова: {', '.join(self.used_words)}"
