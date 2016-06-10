import random
import sys

import nltk

KEY_ADJACENCY_LIST_FILE_NAME = 'keys.adj'


# read in key adjacency list
def read_adjacency_list(filename):
    mapping = {}
    with open(filename) as adjacency_list:
        for line in adjacency_list:
            if len(line) > 1:
                keys = line.split()
                mapping[keys[0]] = keys[1:]
    return mapping


def typo(input_text):
    # read in input sentence and tokenize
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
    return new_text


KEY_MAPPING = read_adjacency_list(KEY_ADJACENCY_LIST_FILE_NAME)

print(typo(sys.argv[1]))
