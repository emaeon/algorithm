import sys

input=sys.stdin.readline

lst=[]
for _ in range(10):
    a=int(input().rstrip())
    num = a%42
    lst.append(num)
    
print(len(set(lst)))
