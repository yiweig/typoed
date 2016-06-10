import itertools
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


# finds a replacement letter based on the given key mapping
def get_replacement(character, key_mapping):
    if character in key_mapping:
        possible_replacements = key_mapping[character.lower()]
        new_letter = random.choice(possible_replacements)
        if character.isupper():
            new_letter = new_letter.upper()
        return new_letter
    else:
        return character


# pairwise function from itertools recipes page
# https://docs.python.org/3/library/itertools.html#itertools-recipes
def pairwise(iterable):
    """s -> (s0,s1), (s1,s2), (s2, s3), ..."""
    a, b = itertools.tee(iterable)
    next(b, None)
    return zip(a, b)


# create typos using nltk's tokens
# (slower but more flexibility for future augmentation)
def typo_by_token(input_text, key_mapping):
    # read in input sentence and tokenize
    tokens = nltk.word_tokenize(input_text)

    # for each word randomly select a letter and then randomly replace it with its adjacent letter
    new_words = []
    for token in tokens:
        characters = list(token)
        length = len(characters)

        selected_index = random.randint(0, length - 1)
        selected_characters = characters[selected_index]

        new_character = get_replacement(selected_characters, key_mapping)

        characters[selected_index] = new_character
        word = ''.join(characters)
        new_words.append(word)

    new_text = ' '.join(new_words)
    return new_text


# create typos using delimiters in the text
# (faster but less flexible)
def typo_by_delimiter(input_text, key_mapping, delimiter=' '):
    # break input into individual characters, and find indices of delimiters
    characters = list(input_text)
    indices = [index for index, character in enumerate(characters) if character == delimiter]
    # since we want the indices in between the delimiters, add 0 and length-1
    # to the beginning and end of the list, respectively
    indices.insert(0, 0)
    indices.append(len(characters))

    # for each consecutive pair of indices, randomly select an index to replace
    for begin, end in pairwise(indices):
        selected_index = random.randint(begin + 1, end - 1)
        selected_character = characters[selected_index]
        new_character = get_replacement(selected_character, key_mapping)
        characters[selected_index] = new_character

    new_text = ''.join(characters)
    return new_text


KEY_MAPPING = read_adjacency_list(KEY_ADJACENCY_LIST_FILE_NAME)
old_text = sys.argv[1]
typoed_text = typo_by_delimiter(old_text, KEY_MAPPING)
print(typoed_text)
