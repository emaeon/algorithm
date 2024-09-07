import sys

input=sys.stdin.readline

lst=[]
for _ in range(9):
    a=int(input().rstrip())
    lst.append(a)
    
print(max(lst))
print(lst.index(max(lst))+1)
