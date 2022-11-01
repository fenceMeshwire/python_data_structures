#!/usr/bin/env python3

# Python 3.9.5

# 05_sorting_dict_lambda.py

# Purpose: Sorting a list of dictionaries by their keys, values using the lambda function.

stocks = [
    {'stock': 'Unilever', 'value': 47, 'isin': 'GB00B10RZP78'},
    {'stock': 'Golden Ocean', 'value': 10, 'isin': 'BMG396372051'},
    {'stock': 'Altria', 'value': 46, 'isin': 'US02209S1033'},
    {'stock': 'Imperial Brands', 'value': 22, 'isin': 'GB0004544929'},
]

stocks_by_stock = sorted(stocks, key=lambda s: s['stock'])
print(stocks_by_stock)

stocks_by_value = sorted(stocks, key=lambda v: v['value'])
print(stocks_by_value)

stocks_by_isin = sorted(stocks, key=lambda v: v['isin'])
print(stocks_by_isin)
