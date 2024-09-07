import sys

input = sys.stdin.readline

n = int(input().rstrip())
lst = list(map(int,input().split()))

num=0
for i in range(n) :
    k = lst[i]/max(lst)*100
    num += k

print(num/n)