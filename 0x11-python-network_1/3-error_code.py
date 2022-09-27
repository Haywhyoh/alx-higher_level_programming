#!/usr/bin/python3
"""This docs is useless"""
import urllib.request
import urllib.error
import sys

if __name__ == "__main__":
    #we try the request
    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            body = response.read().decode('utf-8')
            print(body)
    except urllib.error.HTTPError as e:
        code = e.code
        print("Error code:{:d}".format(code))
