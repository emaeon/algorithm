import sys

input = sys.stdin.readline

a = int(input().rstrip())

lst=[]
for i in range(1,a-1):
    temp = i * (a-1-i)
    print(temp)
    lst.append(temp)
    
print(sum(lst))
print(3)