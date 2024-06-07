import sys

input = sys.stdin.readline

a = list(str(input().rstrip()))

print(*sorted(a, reverse=True), sep='')