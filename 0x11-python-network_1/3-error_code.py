#!/usr/bin/python3
"""
script that takes in a URL, sends a POST request to the URL
with the email as a paramete,
and displays the body of the response
"""
import urllib.parse
import urllib.request
import urllib.error
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            the_page = response.read()
            print(the_page.decode('utf8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
