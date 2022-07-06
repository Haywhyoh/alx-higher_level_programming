#!/usr/bin/python3
def pascal_triangle(n):
    # eturns a list of lists of integers representing the Pascal’s triangle of n
    # Returns an empty list if n <= 0
    pascal = []
    d = 0
    if n <= 0:
        return pascal
    for i in range(1, n+1):
        if i == 1:
            pascal.append(i)
            print(pascal)
            i += 1
        if i == 2:
            pascal.append(1)
            print(pascal)
        (pascal_d[d] for elem in pascal   )

 