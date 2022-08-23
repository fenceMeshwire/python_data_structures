#!/usr/bin/env python3

# Python 3.9.5

01_ordered_dictionary.py

# Dependencies
from collections import OrderedDict
import json

ord_d = OrderedDict()
ord_d['four'] = 1
ord_d['times'] = 2
ord_d['a'] = 3
ord_d['charm'] = 4

print(ord_d)
# OrderedDict([('four', 1), ('times', 2), ('a', 3), ('charm', 4)])

for key in ord_d:
    print(key, ord_d[key])

# Convert ord_d into a json string:
json_string = json.dumps(ord_d)

# Convert json_string into a dictionary:
ord_dict = json.loads(json_string)

type(ord_dict) 
# <class 'dict'>

# --------------------------------------------
# ALTERNATIVELY:
dict(ord_d)
# {'four': 1, 'times': 2, 'a': 3, 'charm': 4}
type(dict(ord_d))
# <class 'dict'>
