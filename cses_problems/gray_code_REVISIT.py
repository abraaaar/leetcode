"""
TODO: recursion in python, pointer passing, left shift, right shift, ADDING TO LIST ELEMENTS, map, list functions 
Source: https://cses.fi/problemset/task/2205
Gray Code
CONCEPT: two concepts one is that take n, add prefix 0, reverse n, add prefix 1

2nd is gray code formula
"""
import sys
data = sys.stdin.read().split()
if data:
    n = int(data[0])
else:
    sys.exit()

l = ["0", "1"]
for i in range(n - 1):
    one = list(map(lambda item: f"0{item}", l))
    rev = l[::-1]
    two = list(map(lambda item: f"1{item}", rev))
    one.extend(two)
    l = one

print(*l, sep="\n")


# for _ in range(n - 1):
#     one = [f"0{item}" for item in l]    
#     two = [f"1{item}" for item in l[::-1]]
#     l = one + two
# # If n=1, the loop never runs, and it prints the base case ["0", "1"]
# sys.stdout.write("\n".join(l) + "\n")


# for i in range(1 << n):
#     # 1. Apply the Gray Code formula: G(i) = i XOR (i shifted right by 1)
#     gray = i ^ (i >> 1)
    
#     # 2. Format the number into a binary string of length n
#     # {gray:0{n}b} tells Python: 
#     # - format 'gray' as binary ('b')
#     # - make it length 'n'
#     # - pad with zeros ('0')
#     sys.stdout.write(f"{gray:0{n}b}\n")