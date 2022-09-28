#!/usr/bin/python3
"""A script that
- takes in a URL
- sends a request to the URL
- displays the body of the response.
"""
import sys
import requests


if __name__ == "__main__":
    #set the url in the address
    url = sys.argv[1]
    #get the request neeed with url as parameter
    r = requests.get(url)
    #check if the status_code is 404
    if r.status_code >= 400:
        #if r.status_code >=400
        #print error coded
        print("Error code: {}".format(r.status_code))
    else:
        #ifno error code print r.text
        print(r.text)
