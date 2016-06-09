import random
import sys

import nltk

KEY_ADJACENCY_LIST_FILE_NAME = 'keys.adj'
KEY_MAPPING = {}

# read in key adjacency list
with open(KEY_ADJACENCY_LIST_FILE_NAME) as adjacency_list:
    for line in adjacency_list:
        if len(line) > 1:
            keys = line.split()
            KEY_MAPPING[keys[0]] = keys[1:]

# read in input sentence and tokenize
input_text = sys.argv[1]
tokens = nltk.word_tokenize(input_text)

# for each word randomly select a letter and then randomly replace it with its adjacent letter
new_words = []
for token in tokens:
    letters = list(token)
    length = len(letters)

    selected_index = random.randint(0, length - 1)
    selected_letter = letters[selected_index]

    new_letter = random.choice(KEY_MAPPING[selected_letter.lower()])
    if selected_letter.isupper():
        new_letter = new_letter.upper()

    letters[selected_index] = new_letter
    word = ''.join(letters)
    new_words.append(word)

new_text = ' '.join(new_words)

print(new_text)
