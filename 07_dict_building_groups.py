#!/usr/bin/env python3

# Python 3.9.5

# 07_dict_building_groups.py

# Purpose: Sort keys, values from dictionaries in a list to form groups (e.g. date, IP address).

# Dependencies
from operator import itemgetter
from itertools import groupby
from collections import defaultdict

# Some fictional data:
log_file_records = [
    {'date': '07/08/2022', 'IP address': '10.113.188.75'},
    {'date': '08/08/2022', 'IP address': '17.55.36.178'},
    {'date': '04/08/2022', 'IP address': '10.113.288.75'},
    {'date': '07/08/2022', 'IP address': '11.117.222.18'},
    {'date': '06/08/2022', 'IP address': '24.251.247.78'},
    {'date': '06/08/2022', 'IP address': '115.125.250.23'},
    {'date': '04/08/2022', 'IP address': '10.113.249.75'},
    {'date': '07/08/2022', 'IP address': '10.113.189.75'},
    {'date': '08/08/2022', 'IP address': '24.251.247.78'},
]

# 1a. Sort the records by 'date':
log_file_records.sort(key=itemgetter('date'))
# 2a. Loop over the sorted keys, values in the dictionary, with the key 'date'
for date, records in groupby(log_file_records, key=itemgetter('date')):
    print(date)
    for record in records:
        print('[+]', record['IP address'])

# 1b. Sort the records by 'IP address':
log_file_records.sort(key=itemgetter('IP address'))
# 2b. Loop over the sorted keys, values in the dictionary, with the key 'IP address'
for record, dates in groupby(log_file_records, key=itemgetter('IP address')):
    print(record)
    for date in dates:
        print('[+]', date['date'])
