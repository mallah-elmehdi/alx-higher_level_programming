#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if isinstance(a_dictionary, dict):
        key_value_pair = filter(lambda item: item[1] != value, a_dictionary.items())
        return dict(key_value_pair)
