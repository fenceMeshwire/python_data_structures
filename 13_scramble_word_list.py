#!/usr/bin/env python3

# Python 3.9.5

# 13_scramble_word_list.py

# Purpose: Mix up the words of a previously ordered list of words.

# Dependency
import random

words:list = ['apple', 'atomic', 'baloo', 'bear', 'book', 'charlene', 'chip', 'crane', 'dale', 'duck']

random_word_index:list = []
random_words:list = []

i = 0
while i <= len(words):
    random_word = random.randint(0, len(words))
    if random_word not in random_word_index:
        random_word_index.append(random_word)
    i = len(random_word_index)

# Map random word index list to words list as a dictionary
mapping:dict = {}
for key, value in zip(random_word_index, words):
    mapping[key] = value

# One-Liner:
# mapping = {mapping[key] for key, value in zip(random_word_index, words)}

for key in sorted(mapping.keys()):
    random_words.append(mapping[key])

# One-Liner:
# random_words = [mapping[key] for key in sorted(mapping.keys())]

print(random_words)
