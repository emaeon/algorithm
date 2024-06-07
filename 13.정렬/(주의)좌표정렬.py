import sys

input = sys.stdin.readline

n = int(input().rstrip())

lst= []
for _ in range(n):
    a = list(map(int, input().split()))
    lst.append(a)

# lst.sort(key = lambda x:x[0])
lst.sort()

for i in lst:
    print(*i, sep=" ")