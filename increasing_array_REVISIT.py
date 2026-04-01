"""
TODO: read about map function in array
Source: https://cses.fi/problemset/task/1094
Increasing array
CONCEPT : just make sure to update the array as you go along

"""
import sys
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))

moves = 0
for i in range(1, len(a)):
    if a[i] < a[i-1]:
        moves += (a[i-1] - a[i])
        a[i] = a[i-1]
print(moves)
