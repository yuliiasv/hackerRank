__author__ = 'jullyt'
#!/bin/python3

import sys

def birthdayCakeCandles(n, ar):
    #return ar.count(max(ar))
    tallestcandles = max(ar)
    candles = 0
    for item in ar:
        if item == tallestcandles:
            candles += 1
    return candles



n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = birthdayCakeCandles(n, ar)
print(result)
