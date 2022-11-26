#!/usr/bin/env python3

# Python 3.9.5

# 12_create_mapped_dict.py

# Purpose: Create a mapped dictionary from a list, using the enumerate() method.

lst = ['cat','art', 'ppu', 'cpu', 'qty']
mapped_dict = {}

for i, v in enumerate(lst):
    mapped_dict[v] = i

print(mapped_dict)
