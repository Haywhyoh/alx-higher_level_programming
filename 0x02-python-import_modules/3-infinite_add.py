#!/usr/bin/python3
import sys

def main():
    argc = len(sys.argv)
    sum = 0
    for i in range(1, argc):
        sum = sum + argv[i]
    print(sum)

if __name__ == "__main__":
    main()
