#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list is not None:
        i = -1
        while i >= -len(my_list):
            print("{:d}".format(my_list[i]))
            i -= 1
