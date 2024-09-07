import sys

input = sys.stdin.readline

x,y,w,h = map(int,input().split())

lst =[x,y]


if w-x >= 0:
    lst.append(w-x)
    
if h-y >= 0:
    lst.append(h-y)
    
lst.sort()

print(lst[0])