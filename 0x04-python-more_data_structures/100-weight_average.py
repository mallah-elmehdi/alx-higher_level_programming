#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    return sum(map(lambda item: item[0] * item[1], my_list)) / sum(
        map(lambda item: item[1], my_list)
    )
