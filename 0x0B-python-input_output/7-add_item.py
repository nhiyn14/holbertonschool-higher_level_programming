#!/usr/bin/python3
"""
a script that adds all arguments to a Python list
and then save them to a file:
"""

import json
import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

try:
    list = load_from_json_file("add_item.json")
except FileNotFoundError:
    list = []

argList = sys.argv[1:]
for arg in argList:
    list.append(arg)

save_to_json_file(list, "add_item.json")
