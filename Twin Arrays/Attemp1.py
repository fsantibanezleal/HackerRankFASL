#!/bin/python3

import sys

def twinArrays(ar1, ar2):
    outTwin = 0
    # Complete this function
    ar1ST = sorted((e,i) for i,e in enumerate(ar1))
    ar2ST = sorted((e,i) for i,e in enumerate(ar2))
    
    if ar1ST[0][1] != ar2ST[0][1]:
        outTwin = ar1ST[0][0] + ar2ST[0][0]
    else:
        outTwin = min(ar1ST[0][0] + ar2ST[1][0], ar1ST[1][0] + ar2ST[0][0])
    return outTwin
    
n = int(input().strip())
ar1 = list(map(int, input().strip().split(' ')))
ar2 = list(map(int, input().strip().split(' ')))

result = twinArrays(ar1, ar2)
print(result)
