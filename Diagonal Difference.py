#!/bin/python3

import sys

def diagonalDifference(a):
    sumFirst = sum(a[i][i] for i in range(n))
    return sumFirst

if __name__ == "__main__":
    n = int(input().strip())
    a = []
    for a_i in range(n):
       a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
       a.append(a_t)
    result = diagonalDifference(a)
    print(result)
