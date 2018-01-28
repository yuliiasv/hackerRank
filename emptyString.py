#!/bin/python

import sys

def super_reduced_string(s):
    changed = True
    while changed:
        i = 0
        l =len(s)
        changed  = False
        while i < l:
            if i != l-1 and s[i] == s[i+1] :
                if i == 0 :
                    s = s[i+2:]  
                else:
                    s = s[:i] + s [i+2:]
                l = len(s)
                changed = True
            else:
                i += 1
    if len(s) == 0:
        return 'Empty String'
    else:
        return s
            
                
        

s = input().strip()
result = super_reduced_string(s)
print(result)

