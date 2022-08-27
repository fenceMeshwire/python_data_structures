#!/usr/bin/env python3

# Python 3.9.5

# Dependency
from types import MappingProxyType

dict = {'alpha': 1, 'beta': 2}
proxy_dict = MappingProxyType(dict)

print(proxy_dict)
print(proxy_dict['alpha'])
print(proxy_dict['beta'])

# Add additional key, value to dict
dict['gamma'] = 3

# A proxy dictionary reflects all dictionary values. 
# Proxy dictionaries are immutable and cannot be changed.
# To change the proxy dictionary, the dictionary must be changed first.

print(proxy_dict)
