"""
TODO: learn List Comprehension 
Source: https://cses.fi/problemset/task/1092
Two Sets
CONCEPT : go from n to 1 and check whether the sum if getting bigger than half
then make another set by using smart list comprehension
"""
import sys

n = int(sys.stdin.readline())

total = n * (n + 1) // 2
if total % 2 != 0:
    print("NO")
    exit()

print("YES")

half = total // 2


set1 = []
s = 0
for i in range(n, 0, -1):
    if s + i <= half:
        set1.append(i)
        s += i
    if s == half:
        break

set2 = [x for x in range(1, n + 1) if x not in set(set1)]

print(len(set1))
print(*set1)
print(len(set2))
print(*set2)