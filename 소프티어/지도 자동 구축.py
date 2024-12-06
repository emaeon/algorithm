import sys
import math

input = sys.stdin.readline
n = int(input().rstrip())

# 규칙 : 2*2 -> 3*3 -> 5*5 -> 9*9 즉, n + (n-1)
first = 3
if n >= 2:

    for i in range(1, n):
        first = first + (first - 1)
    print(int(math.pow(first, 2)))

else:
    print(int(math.pow(3, 2)))