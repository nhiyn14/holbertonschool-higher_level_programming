#!/usr/bin/python3
def no_c(my_string):
    new_string = ""
    remove = "cC"
    for i in range(len(my_string)):
        if my_string[i] not in remove:
            new_string = new_string + my_string[i]
    return new_string
