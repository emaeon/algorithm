import sys

input = sys.stdin.readline

n = int(input().rstrip())

lst = []
for _ in range(n):
    a=input().rstrip()
    lst.append([a,len(a)])
    
lst.sort(key = lambda x:(x[1], x[0]))

lst2=[]
for i in lst:
    
    if i[0] in lst2:
        pass
    else:
        lst2.append(i[0])

for j in lst2:
    print(j)