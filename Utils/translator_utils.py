from googletrans import Translator
from collections import Counter

translator = Translator()

async def translate_titles(titles):
    translated = []
    for title in titles:
        result = await translator.translate(title, dest='en')
        translated.append(result.text)
    return translated

def find_repeated_words(translated_titles):
    all_words = " ".join(translated_titles).split()
    counter = Counter(word.lower() for word in all_words)
    repeated = {word: count for word, count in counter.items() if count > 2}
    return repeated