import sys
from collections import deque
input = sys.stdin.readline


def bfs(si,sj) :
    q = deque()
    q.append((si,sj))
    v[si][sj] = 1
    
    while q :
        ti,tj = q.popleft()
        for idx in range(4):
           ni = ti + dx[idx] 
           nj = tj + dy[idx] 
           if (0<=ni<n) and (0<=nj<m) and (v[ni][nj]==0) and(arr[ni][nj]==1) :
               q.append((ni,nj))
               v[ni][nj] = 1
        


t = int(input().rstrip())

dx=[-1,1,0,0]
dy=[0,0,-1,1]

for test in range(t) :
    m,n,k = map(int,input().split()) #열, 행, 위치
    arr = [[0]*m for _ in range(n)]
    v = [[0]*m for _ in range(n)]
    cnt = 0
    for _ in range(k) :
        x,y = map(int,input().split())
        arr[y][x] = 1
        
    for i in range(n):
        for j in range(m) :
            if v[i][j] == 0 and arr[i][j]== 1:
                bfs(i,j)
                cnt += 1
    print(cnt)
        
        
    



