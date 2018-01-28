#!/bin/python3
#input 10
#s = 'beabeefeab'
import sys

def getUniquePairs(uniq):
    f = {}
    for i in uniq:
        for j in uniq:
            if i != j:
                key = i+j
                key2 = j+i
                if not (key2 in f):
                    f[key] = [i, j]
    return f

def prepareString(inputString, pair):
    k = ''
    l = len(inputString)
    for i in range (0, l):
        if inputString[i] == pair[0] or inputString[i] == pair[1]:
            k = k + inputString[i]
    return k

def isSuitableString(preparedStr):
    g = len(preparedStr) - 1
    for i in range(0, g):
        if preparedStr[i] == preparedStr[i + 1]:
            return False
    return True
    
def twoCharaters(s):
    unique = {ch for ch in s}
    f = getUniquePairs(unique)
    new_list = []
    for key in f:
        preparedStr = prepareString(s, f[key])
        isSuitable = isSuitableString(preparedStr)
        if isSuitable:
            new_list.append(preparedStr)

    max_length = [0]
    for i in new_list:
        max_length.append(len(i))
   
    return  max(max_length)




if __name__ == "__main__":
    l = int(input().strip())
    s = input().strip()
    result = twoCharaters(s)
    print(result)
