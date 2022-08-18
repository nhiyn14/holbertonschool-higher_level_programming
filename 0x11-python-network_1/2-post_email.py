#!/usr/bin/python3
"""
script that takes in a URL and email
sends a POST request to the URL
with the email as a paramete
and displays the body of the response(decoded in utf-8)
"""
import urllib.parse
import urllib.request
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    value = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(value).encode('utf-8')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        the_page = response.read()
    print(the_page.decode('utf8'))
