import sys
 
input = sys.stdin.readline

n = int(input().rstrip())
lst = list(map(str, input().split()))

x = 1
y = 1
#L,R,U,D
dx = [0,0,-1,1]
dy = [-1,1,0,0]
idx = ['L','R','U','D']

for i in lst:
    temp = idx.index(i)
    
    if x + dx[temp] < 1 or x + dx[temp] > n or y + dy[temp] < 1 or y + dy[temp] > n:
        continue
    else:
        x += dx[temp]
        y += dy[temp]
        
print(x,y)
     
 
 
 