#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if isinstance(a_dictionary, dict):
        key_value_pair = list(filter(lambda e: e[1] == value, a_dictionary.items()))
        for key in key_value_pair:
            del a_dictionary[key[0]]
        return dict(a_dictionary)
