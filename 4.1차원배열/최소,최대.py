import sys

input=sys.stdin.readline

n = int(input().rstrip())
lst=list(map(int,input().split()))

max_a = max(lst)
min_a = min(lst)

print(min_a, max_a)