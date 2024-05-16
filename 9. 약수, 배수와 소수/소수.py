import sys

input=sys.stdin.readline

m = int(input().rstrip())
n = int(input().rstrip())

lst=[]
if m == 2 :
    lst.append(m)
    for i in range(m+1,n+1):  
        for j in range(2,i):
            if i % j == 0:
                break
            elif j == i-1:
                lst.append(i)
else:
    for i in range(m,n+1):
        for j in range(2,i):
            if i % j == 0:
                break
            elif j == i-1:
                lst.append(i)
            
lst.sort()
print(lst)
if len(lst) <1 :
    print(-1)
else:
    print(sum(lst))
    print(lst[0])
