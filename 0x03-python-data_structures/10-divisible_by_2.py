#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = []
    for e in my_list:
        new_list.append(e % 2 == 0)
    return new_list
