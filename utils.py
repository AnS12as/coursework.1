# utils.py

import requests
from basic_word import BasicWord

def load_random_word():
    json_url = "https://jsonkeeper.com/b/K73Q"  # Заменить на URL JSON
    response = requests.get(json_url, verify=False)

    if response.status_code == 200:
        data = response.json()
        if isinstance(data, list) and len(data) > 0:
            # Взять первый элемент из списка
            word_data = data[0]

            return BasicWord(word_data["word"], word_data["subwords"])
        else:
            return BasicWord("default_word", [])
    else:
        return BasicWord("default_word", [])
