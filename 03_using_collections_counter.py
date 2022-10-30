#!/usr/bin/env python3

# Python 3.9.5

# 03_using_collections_counter.py

# Purpose: Using the counter from collections to count e.g. letters from a string.

# Dependency
from collections import Counter

letters_a = Counter('Bubblegum')
letters_b = Counter('Chewbacca')

# Define the number of most common elements
mce = 3
three_mc = letters_a.most_common(mce)
print(three_mc)

# Combination
combination = letters_a + letters_b
print(combination)

# Subtraction
subtraction = letters_a - letters_b
print(subtraction)
