import sys

input = sys.stdin.readline

n = int(input().rstrip())

lst=[]
for _ in range(n):
    temp = int(input().rstrip())
    lst.append(temp)
    
lst.sort()

print(*lst, sep='\n')