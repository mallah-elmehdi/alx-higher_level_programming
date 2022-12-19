#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    res = 0
    i = 0
    while i < x:
        try:
            print("{:d}".format(my_list[i]), end="")
            res += 1
        except (ValueError, TypeError, IndexError):
            pass
        i += 1
    print("")
    return res
