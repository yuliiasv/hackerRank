#!/bin/python3

import sys

def hackerrankInString(s):
    p = 0
    for i in 'hackerrank':
        if i in s[p:]:
            p = s.index(i,p) + 1
        else:
            return 'NO'
    return 'YES'
                           
                

if __name__ == "__main__":
    q = int(input().strip())
    for a0 in range(q):
        s = input().strip()
        result = hackerrankInString(s)
        print(result)

