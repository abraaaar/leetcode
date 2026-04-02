# Source: https://cses.fi/problemset/task/1068
#Weird Algorithm
import math
n = int(input())
while(n != 1):
    if (n%2 == 0):
        n //= 2
    else:
        n = n*3 + 1
    print(n, end = ""  if n == 1 else " ")   

