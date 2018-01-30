__author__ = 'yuliia'
"""Given an array of integers, calculate which fraction of its elements are positive, which fraction of its elements are negative,
 and which fraction of its elements are zeroes, respectively. Print the decimal value of each fraction on a new line."""
#!/bin/python3

import sys

def plusMinus(arr):
    negativeNumbersAmount = 0
    positiveNumbersAmount = 0
    zeroAmount = 0
    for i in arr:
        if i == 0:
            zeroAmount += 1
        elif i > 0:
            positiveNumbersAmount += 1
        else:
            negativeNumbersAmount += 1
    print(format(positiveNumbersAmount/len(arr),'.6f'))
    print(format(negativeNumbersAmount/len(arr),'.6f'))
    print(format(zeroAmount/len(arr),'.6f'))
    # Complete this function

if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    plusMinus(arr)
