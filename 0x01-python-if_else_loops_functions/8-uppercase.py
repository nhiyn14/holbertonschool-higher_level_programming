#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        c = ord(str[i])
        if c >= 97 and c <= 122:
            c = c - 32
        c = chr(c)
        print(f"{c}", end='')
    print()
