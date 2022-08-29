#!/usr/bin/env python3

# Python 3.9.5

# 06_get_unique_items_list.py

duplicates = ['Paul', 'Jenny', 'Sally', 'James', 'Paul', 'Sam', 'Sam', 'Sally', 'Jenny']

# First convert the list to a set, to get the unique items:
unicates_set = set(duplicates)
print(unicates_set)

# Next convert the set back to a list:
unicates_list = list(set(unicates_set))
print(unicates_list)

# Finally sort the list of unique items:
print(sorted(unicates_list))
