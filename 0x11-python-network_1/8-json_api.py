#!/usr/bin/python3
"""
script that takes in a letter to variable 'q'
sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter
If no argument is given, set q=""
if right format, display: [<id>] <name>
"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) < 2:
        q = ""
    else:
        q = sys.argv[1]

    req = requests.post('http://0.0.0.0:5000/search_user', data={'q': q})

    try:
        req_dict = req.json()
        if bool(req_dict) is False:
            print("No result")
        else:
            print("[{}] {}".format(req_dict['id'], req_dict['name']))
    except Exception:
        print("Not a valid JSON")
