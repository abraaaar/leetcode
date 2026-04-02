"""
TODO: learn about pow modulo and zfill() and conversions
Source: https://cses.fi/problemset/task/1617
Bit Strings
CONCEPT : just convert the binary to integer, do normal addition and 
then convert back to binary
"""
import sys

n = int(sys.stdin.readline())
MOD = 10**9 + 7
print(pow(2, n, MOD))

s = "".zfill(n)
print(s)

while (s != "1" * n):
    s = int(s, 2) + 1
    s= bin(s)[2:].zfill(n)
    print(s, end = "" if s=="1"*n else "\n")
