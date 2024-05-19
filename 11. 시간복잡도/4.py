import sys

input = sys.stdin.readline


a = int(input().rstrip())
sum = 0
for i in range(1,a):
    sum += i
print(sum)
print(2)    