#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary == None:
        return None
    return sorted(a_dictionary.items(), key=lambda item: item[1], reverse=True)[0][0]
