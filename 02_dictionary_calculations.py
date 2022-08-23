#!/usr/bin/env python3

# Python 3.9.5

# 02_dictionary_calculations.py

material_prices = {
   'copper': 30.50,
   'PVC': 21.95,
   'CPVC': 17.85,
   'PEX': 19.5,
   'stainless steel': 45.69
}

type(material_prices.values())
# <class 'dict_values'>
type(material_prices.keys())
# <class 'dict_keys'>

# Return the lowest plumbing material price
min_mat_price = min(zip(material_prices.values(), material_prices.keys()))
print(min_mat_price)

# Return the highest plumbing material price
max_mat_price = max(zip(material_prices.values(), material_prices.keys()))
print(max_mat_price)

# Return of material prices in ascending order
prices_sorted = sorted(zip(material_prices.values(), material_prices.keys()))
print(prices_sorted)
