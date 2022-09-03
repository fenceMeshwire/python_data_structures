#!/usr/bin/env python3

# Python 3.9.5

# 08_enumerate.py

# Enumerate a list object
lst = ['Convertible', 'Coupe', 'Hatchback', 'MUV', 'Pickup Truck', 'SUV', 'Sedan']
enum_lst = enumerate(lst)
print(list(enum_lst))

# Looping over the enumeration, it works only in this manner (for i in enum_lst: does not produce any output).
# -> Looping and enumaration a list must take place in the same step.
for i in enumerate(lst):
  print(i)
  print(type(i)) # The output for each element is a tuple, which is immutable (not changeable).

# Separation of position number and position value:
for num, value in enumerate(lst):
    print(num, value)
