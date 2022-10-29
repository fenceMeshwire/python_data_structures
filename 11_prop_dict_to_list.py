#!/usr/bin/env python3

# Python 3.9.5

# 11_prop_dict_to_list.py

# Purpose: Prop down integrated dictionaries to lists, keeping the values without the keys.

order = [
    {'cat': 1, 'art': 'beer', 'ppu': 4.2, 'cpu': 4.2, 'qty': 1},
    {'cat': 1, 'art': 'water', 'ppu': 1.8, 'cpu': 1.8, 'qty': 1},
    {'cat': 1, 'art': 'water big', 'ppu': 3.0, 'cpu': 3.0, 'qty': 1},
    {'cat': 1, 'art': 'juice', 'ppu': 3.9, 'cpu': 3.9, 'qty': 1},
    {'cat': 1, 'art': 'main dish 1', 'ppu': 13.5, 'cpu': 13.5, 'qty': 1},
    {'cat': 1, 'art': 'main dish 2', 'ppu': 15.5, 'cpu': 15.5, 'qty': 1}
    ]

# Prop down integrated dictionaries to lists:
simplified_order = []
for item in order:
    position = []
    position = [value for key, value in item.items()]
    simplified_order.append(position)
    
# Show result
print(simplified_order)
