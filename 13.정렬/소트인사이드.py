import sys

input = sys.stdin.readline

n =input().rstrip()

print(*sorted(n,reverse=True),sep='')