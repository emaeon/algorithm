import sys

input = sys.stdin.readline

lst = [0]*10001

n = int(input())

for _ in range(n):
    lst[int(input())] +=1
    
for i in range(10000):
    if lst[i] != 0 :
        for _ in range(lst[i]):
            print(i)