#!/usr/bin/env python3
# Author ID: [mrdhakal]

# Dictionaries
dict_york = {'Address': '70 The Pond Rd', 'City': 'Toronto', 'Country': 'Canada', 'Postal Code': 'M3J3M6', 'Province': 'ON'}
dict_newnham = {'Address': '1750 Finch Ave E', 'City': 'Toronto', 'Country': 'Canada', 'Postal Code': 'M2J2X5', 'Province': 'ON'}
# Lists
list_keys = ['Address', 'City', 'Country', 'Postal Code', 'Province']
list_values = ['70 The Pond Rd', 'Toronto', 'Canada', 'M3J3M6', 'ON']

def create_dictionary(keys, values):
    # Place code here - refer to function specifics in section below

    res = {}
    for key, value in zip(keys, values):
        res[key] = value
    
    return res

def shared_values(dict1, dict2):
    # Place code here - refer to function specifics in section below
    set_one = set(dict1.values())
    set_two = set(dict2.values())
    
    # Find the intersection of the two sets to get shared values
    shared = set_one.intersection(set_two)
    
    return shared


if __name__ == '__main__':
    york = create_dictionary(list_keys, list_values)
    print('York: ', york)
    common = shared_values(dict_york, dict_newnham)
    print('Shared Values', common)