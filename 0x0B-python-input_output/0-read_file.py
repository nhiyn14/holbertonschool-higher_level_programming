#!/usr/bin/python3
"""
function that reads a text file (UTF8) and prints it to stdout:
"""


def read_file(filename=""):
    """read text file and print to stdout"""
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")