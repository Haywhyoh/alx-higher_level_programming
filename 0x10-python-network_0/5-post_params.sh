#!/bin/bash
#curl sends POST req to URL, display response body
curl -s -X POST -d "email=test@gmail.com&subject=I will always be there for PLD" "$1"
