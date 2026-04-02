"""
TODO: learn deque from collections
learn unpacking *
Source: https://cses.fi/problemset/task/1070
Permutations
CONCEPT : print evens first then odds
"""
import sys
n = int(sys.stdin.readline())
# if n == 2 or n == 3:
#     print("NO SOLUTION", end="")
#     exit()

# if n == 1:
#     print(1, end="")
#     exit()

# for i in range(2, n+1, 2):
#     print(i, end = " ")
# for i in range(1, n+1, 2):
#     print(i, end="" if i==n else " ")

if n == 1:
    print(1)
elif n < 4:
    print("NO SOLUTION")
else:
    print(*range(2, n+1, 2), *range(1, n+1, 2))