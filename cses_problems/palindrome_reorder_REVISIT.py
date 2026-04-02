"""
TODO: learn hashmap and COUNTER and [::-1] traversal
Source: https://cses.fi/problemset/task/1755
Palindrome Reorder
CONCEPT : use list as stings are immutable
insert half in left then mid and then reverse the left half 
"""
import sys
# from collections import Counter
from collections import defaultdict
s = sys.stdin.readline().strip()
freq = defaultdict(int)
for char in s:
    freq[char] += 1

half = []
odd_count = 0
odd_char = ''
for char, num in freq.items():
    if num%2 != 0:
        odd_count+=1
        if odd_count > 1:
            print("NO SOLUTION", end = "")
            exit()
        odd_char = char
    
    half.append(char * (num//2))

left = "".join(half)
res = left+odd_char+left[::-1]

print(res, end = "")


    


