#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    i = 0
    new_list = []
    while i < list_length:
        try:
            new_list.append(0)
            new_list[i] = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
        except (TypeError, ValueError):
            print("wrong type")
        except IndexError:
            print("out of range")
        finally:
            pass
        i += 1
    return new_list
