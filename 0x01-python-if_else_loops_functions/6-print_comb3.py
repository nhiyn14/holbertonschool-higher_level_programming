#!/usr/bin/python3
for i in range(0, 11):
    for x in range(i+1, 10):
        if i == 8:
            print(f"{i}{x}")
        else:
            print(f"{i}{x}", end=', ')
