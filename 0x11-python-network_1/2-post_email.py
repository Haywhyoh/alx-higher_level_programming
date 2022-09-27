#!/usr/bin/python3
"""
Python script that takes in a URL and an email, sends a POST
request to the passed URL with the email as a parameter, and
displays the body of the response
"""
from urllib import request,parse
import sys


if __name__ == "__main__":
    #declare values as a dictionary
    values = {'email' : sys.argv[2]}
    # urlencode andd parse the calues
    data = parse.urlencode(values)
    #encode the data to ascii
    data = data.encode('ascii')
    #request the page with the Request Class
    req = request.Request(sys.argv[1], data)
    #get response with urlopen
    with request.urlopen(req) as response:
        html = response.read()
        print(html.decode('utf-8'))
