import sys

input=sys.stdin.readline

m = int(input().rstrip())
n = int(input().rstrip())

lst=[]

for i in range(m,n+1):
    if i ==1:
        continue
    elif i == 2:
        lst.append(2)
    else:
        for j in range(2,i+1):
            if j != i and i % j == 0:
                break
            elif j == i:
                lst.append(i)
            
lst.sort()
# print(lst)
if len(lst) <1 :
    print(-1)
else:
    print(sum(lst))
    print(lst[0])