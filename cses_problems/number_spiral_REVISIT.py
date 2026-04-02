"""
Source: https://cses.fi/problemset/task/1071
Number Spiral
CONCEPT : current layer is max of y and x, make the formula
"""
import sys
t = int(sys.stdin.readline())
queries = []
for _ in range(t):
    y, x = map(int, sys.stdin.readline().split())
    queries.append((y, x))
for y, x in queries:
    layer = max(y,x)
    sq = layer*layer
    sq2 = (layer-1)*(layer-1)
    if layer%2 == 0:
        if y == layer:
            print(sq + 1 - x)
        else:
            print(sq2 + y)
    else:
        if x == layer:
            print(sq+1-y)
        else:
            print(sq2+x)
    