#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary == None or len(a_dictionary) == 0:
        return None
    sort = sorted(a_dictionary.items(), key=lambda i: i[1], reverse=True)
    return sort[0][0]
