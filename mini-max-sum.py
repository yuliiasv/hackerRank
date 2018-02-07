__author__ = 'jullyt'
#!/bin/python3

import sys

def miniMaxSum(arr):
    minValue = sum(sorted(arr)[:-1]) if arr else 0
    maxValue = sum(sorted(arr)[1:]) if arr else 0
    print(minValue, maxValue)

if __name__ == "__main__":
    arr = list(map(int, input().strip().split(' ')))
    miniMaxSum(arr)