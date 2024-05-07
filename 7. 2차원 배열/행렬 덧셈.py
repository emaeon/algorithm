import sys

input=sys.stdin.readline

#행렬크기 
n,m=map(int,input().split())

a=[]
for _ in range(n):
    a.append(list(map(int,input().split())))
b=[]    
for _ in range(n):
    b.append(list(map(int,input().split())))


for i in range(n):
    lst=[]
    for j in range(m):
        lst.append(a[i][j] + b[i][j])
    print(*lst)
    
