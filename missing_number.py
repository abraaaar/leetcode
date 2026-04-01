# Source: https://cses.fi/problemset/task/1083
#Missing number

#CONCEPT : SUM USING AP - ACTUAL SUM

import sys

n = int(sys.stdin.readline())
nums = map(int, sys.stdin.readline().split())

s = sum(nums)
aps = n*(n+1)//2
print(aps-s)

