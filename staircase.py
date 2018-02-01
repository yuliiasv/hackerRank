__author__ = 'jullyt'
#!/bin/python3
"""Observe that its base and height are both equal to ,
and the image is drawn using # symbols and spaces.
The last line is not preceded by any spaces.
Write a program that prints a staircase of size n ."""
"""i = 1
    while i <= n:
        new = i * '#'
        i += 1
        print(('{:>'+str(n)+'}').format(new))"""
import sys

def staircase(n):

    for i in range (1,n+1):
        print(('{:>'+str(n)+'}').format(i * '#'))

    # Complete this function

if __name__ == "__main__":
    n = int(input().strip())
    staircase(n)

