#!/usr/bin/env python3

# Python 3.9.5

# 03_using_collections_counter.py

# Dependency
import collections

letter_count = collections.Counter('Bubblegum')
print(letter_count)

# Define the number of most common elements
mce = 3
three_mc = letter_count.most_common(mce)
print(three_mc)
