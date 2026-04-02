"""
TODO: revise
Source: https://cses.fi/problemset/task/1754
Coin Piles
CONCEPT : sum of both should be divisible by 3 and also one should not be larger than 2x the other
"""
import sys
raw_data = sys.stdin.read().split()
if raw_data:
    t = int(raw_data[0])
    
    test_cases = []
    for i in range(1, 2 * t + 1, 2):
        a = int(raw_data[i])
        b = int(raw_data[i+1])
        test_cases.append((a, b))

    for a, b in test_cases:
        sys.stdout.write("NO\n" if (a+b)%3 != 0 or a>2*b or b>2*a else "YES\n")