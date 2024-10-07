import sys
from collections import deque
input = sys.stdin.readline

n = int(input().rstrip())
arr = []
for _ in range(n) :
    temp = list(map(int,input().split()))
    arr.append(temp)
    
v = [[0]*n for _ in range(n)]

def bfs(si,sj,r) :
    q = deque()
    q.append((si,sj))
    v[si][sj]= 1
    
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    
    while q :
        
        ti,tj = q.popleft()
        
        for idx in range(4):
            nx = ti + dx[idx]
            ny = tj + dy[idx]
            if(0<=nx<n) and (0<=ny<n) and (v[nx][ny]==0) and (arr[nx][ny]>r) :
                q.append((nx,ny))
                v[nx][ny] = 1

result = []

for rain in range(101) :
    cnt = 0
    v = [[0]*n for _ in range(n)]
    
    for i in range(n) :
        for j in range(n) :
            if (v[i][j]==0) and (arr[i][j]>rain) :
                bfs(i,j,rain)
                cnt  += 1
                
    result.append(cnt)
result
print(max(result))

