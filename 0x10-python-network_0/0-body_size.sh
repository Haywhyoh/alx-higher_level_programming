#!/bin/bash
#Script that shpws the Content-Length from a HTTP request
curl -sI  "$1" | grep -i "Content-Length" | cut  -f2 -d ":"
