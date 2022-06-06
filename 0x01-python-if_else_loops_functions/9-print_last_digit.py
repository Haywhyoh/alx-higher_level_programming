#!/usr/bin/python3
def print_last_digit(number):
    if (number < 0):
        number = -number
        last_number = number % 10
        last_number = -last_number
    else:
        last_number = number % 10
    return (last_number)
