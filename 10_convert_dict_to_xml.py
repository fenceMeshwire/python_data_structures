#!/usr/bin/env python3

# Python 3.9.5

# Dependencies
from xml.etree.ElementTree import Element
from xml.etree.ElementTree import tostring

# Data
order = [
    {'cat': 1, 'art': 'beer', 'ppu': 4.2, 'cpu': 4.2, 'qty': 1},
    {'cat': 1, 'art': 'water', 'ppu': 1.8, 'cpu': 1.8, 'qty': 1},
    {'cat': 1, 'art': 'water big', 'ppu': 3.0, 'cpu': 3.0, 'qty': 1},
    {'cat': 1, 'art': 'juice', 'ppu': 3.9, 'cpu': 3.9, 'qty': 1},
    {'cat': 1, 'art': 'main dish 1', 'ppu': 13.5, 'cpu': 13.5, 'qty': 1},
    {'cat': 1, 'art': 'main dish 2', 'ppu': 15.5, 'cpu': 15.5, 'qty': 1}
    ]

# Function
def convert_dict_to_xml(position):
    pos = Element('pos')
    for key, value in position.items():
        child = Element(key)
        child.text = str(value)
        pos.append(child)
    return pos
 
# Determination of the output:
if __name__ == '__main__':
  
  import os
  p = 'C:\\...\\...'  # Set output directory
  os.chdir(p)         # Change working directory to output directory

  with open('output.xml', 'wt') as fout:
      for i in range(len(order)):
          position = order[i]
          xml = convert_dict_to_xml(position)
          xml.set('row', str(i + 1)) 
          fout.write(str(tostring(xml).decode()) + "\n")
