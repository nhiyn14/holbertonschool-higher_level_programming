#!/usr/bin/python3
"""
script that takes in a URL
sends arequest to the URL
and displays the body of the response
If HTTP status code >= 400, print: Error code
"""
import requests
import sys


if __name__ == "__main__":
    req = requests.get(sys.argv[1])
    if req.status_code < 400:
        print(req.text)
    else:
        print("Error code: {}".format(req.status_code))
