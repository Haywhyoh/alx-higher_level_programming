#!/bin/bash
# sends delete req to $1 URL and display response body
curl -s "$1" -X DELETE
