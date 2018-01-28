#!/bin/python3

import sys

def marsExploration(s):
    length = len(s)
    wordCounter = int(length/len('SOS'))
    expectedSignal = 'SOS' * wordCounter
    changedLetter = 0
    for i in range (length):
        if s[i] != expectedSignal[i]:
            changedLetter = changedLetter + 1
    return changedLetter

if __name__ == "__main__":
    s = input().strip()
    result = marsExploration(s)
    print(result)
