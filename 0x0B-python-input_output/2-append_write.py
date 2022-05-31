#!/usr/bin/python3
"""
function that appends a string  at the end of a text file (UTF8)
returns the number of characters added
"""


def append_write(filename="", text=""):
    """append str to text file and return num of char"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
