import sys

input = sys.stdin.readline

n = int(input().rstrip())
lst=[]
for _ in range(n):
    a = int(input().rstrip())
    lst.append(a)
    
lst.sort()

print(*lst, sep='\n')