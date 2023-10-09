#!/usr/bin/python3

def max_integer(my_list=[]):
    if not my_list:
        return None
    new = my_list.copy()
    new.sort()
    return new[-1]
