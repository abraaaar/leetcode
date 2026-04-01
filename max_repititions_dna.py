"""
Source: https://cses.fi/problemset/task/1069
Max repititions
CONCEPT : check for i and i-1 elements
to make sure while iterating the last element is not out of range 

"""
import sys
s = sys.stdin.readline().strip()
m = 1
c = 1
for i in range(1, len(s)):
    if (s[i] == s[i-1]):
        c+=1
        m = max(m, c)
    else:
        c = 1
print(m)