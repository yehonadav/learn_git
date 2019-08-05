import random
import requests

source = requests.get("https://www.phrases.org.uk/meanings/phrases-and-sayings-list.html").text

partial_source = source.split('<div class="content">', maxsplit=1)[1]
partial_source = partial_source.split('<div class="col-md-1"></div>')[0]

mushed_list = partial_source.split('<p class="phrase-list">')
mushed_list = [text.split('>', maxsplit=1)[1] for text in mushed_list]
phrases = [text.split('<', maxsplit=1)[0] for text in mushed_list]
phrase = random.choice(phrases)

print(phrase)
