#!/usr/bin/python3
def complex_delete(a_dict, value):
    if isinstance(a_dict, dict):
        key_value_pair = list(filter(lambda e: e[1] == value, a_dict.items()))
        for key in key_value_pair:
            del a_dict[key[0]]
        return dict(a_dict)
