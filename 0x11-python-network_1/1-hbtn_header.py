#!/usr/bin/python3
""" Python script that takes in a URL, sends a request and displays
the value of the X-Request-Id variable found in the header
"""
import sys
import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as res:
        html = res.info()
print(html.get('X-Request-Id'))
