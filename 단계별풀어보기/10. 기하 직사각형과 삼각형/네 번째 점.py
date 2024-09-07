import sys

input = sys.stdin.readline

lstx=[]
lsty=[]
for _ in range(3):
    x, y = map(int,input().split())
    lstx.append(x)
    lsty.append(y)
    
result=[]
for i in list(set(lstx)):
    if lstx.count(i) == 1:
        result.append(i)

for j in list(set(lsty)):
    if lsty.count(j) == 1:
        result.append(j)
        
print(*result)
