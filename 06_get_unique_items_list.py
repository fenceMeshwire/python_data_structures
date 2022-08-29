#!/usr/bin/env python3

# Python 3.9.5

# 06_get_unique_items_list.py

duplicates = ['Paul', 'Jenny', 'Sally', 'James', 'Paul', 'Sam', 'Sam', 'Sally', 'Jenny']

unicates_set = set(duplicates)
print(unicates_set)

unicates_list = list(set(unicates_set))
print(unicates_list)
print(sorted(unicates_list))
