"""
TODO:  global variable inside function, 
Source: https://cses.fi/problemset/task/2165
Tower of Hanoi
CONCEPT: just do the code for two disks, terminating condition when disks are 0
"""
import sys
data = sys.stdin.read().split()
if data:
    n = int(data[0])
else:
    sys.exit()

def tower(n, st, end, temp):
    if n == 0:
        return
    tower(n - 1, st, temp, end)
    print(f"{st} {end}")
    tower(n - 1, temp, end, st)

print(2**n-1)
tower(n, 1, 3, 2)

