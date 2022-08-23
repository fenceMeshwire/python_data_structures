#!/usr/bin/env python3

# Python 3.9.5

# 02_dictionary_calculations.py

mat_prices = {
   'copper': 30.50,
   'PVC': 21.95,
   'CPVC': 17.85,
   'PEX': 19.5,
   'stainless steel': 45.69
}

type(mat_prices.values())   # <class 'dict_values'>

type(mat_prices.keys())     # <class 'dict_keys'>

min_mat_price = min(zip(mat_prices.values(), mat_prices.keys()))
print(min_mat_price)        # Returns the minimum (value, key)

max_mat_price = max(zip(mat_prices.values(), mat_prices.keys()))
print(max_mat_price)        # Returns the maximum (value, key)

prices_sorted = sorted(zip(mat_prices.values(), mat_prices.keys()))
print(prices_sorted)        # Returns a sorted list [(values, keys)]

# Get the min and max of the dictionary
min(mat_prices)     # Returns the key with minimum value
max(mat_prices)     # Returns the key with maximum value

min(mat_prices.values())
min(mat_prices.keys())

max(mat_prices.values())
max(mat_prices.keys())

# Using the lambda function for determining min and max:
min(mat_prices, key=lambda k:mat_prices[k])
max(mat_prices, key=lambda k:mat_prices[k])

min_mat_price = mat_prices[min(mat_prices, key=lambda k:mat_prices[k])]
max_mat_price = mat_prices[max(mat_prices, key=lambda k:mat_prices[k])]

print(min_mat_price)
print(max_mat_price)
