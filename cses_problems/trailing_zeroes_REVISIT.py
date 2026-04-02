"""
TODO: revise
Source: https://cses.fi/problemset/task/1618
Trailing Zeroes
CONCEPT : compute the number of 5x2 pairs and always number of 5's is 
greater than number of 2's therefore
calculate the number of 5's

but some numbers like 25 125, 625, .. have multiple 5's in them so make logic for that
"""
import sys

n = int(sys.stdin.readline())

res = 0
s = 5
while (s<=n):
    res+=n//s
    s*=5
print(res)
