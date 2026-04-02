"""
TODO: just revision
Source: https://cses.fi/problemset/task/1072
Two Knights
CONCEPT : find total, then calculate 2*3 and 3*2 rectangles 
the total are basically k*kC2
the 2*3 rectangles are (i-1)*(i-2), the 3*2 are also the same, and the attacking pairs are 2 in 1 rectangle each, therefore \
(i-1)*(i-2) *2*2
"""
import sys

n = int(sys.stdin.readline())

for i in range(1, n+1):
    if i == 1:
        print(0)
        continue
    else:
        total = (i*i) * (i*i - 1)//2
        bad = (i-1)*(i-2)*4
        print(total-bad)