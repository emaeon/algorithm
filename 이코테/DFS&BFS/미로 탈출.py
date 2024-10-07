import sys
from collections import deque
n,m = map(int,input().split())

arr = [list(map(int,input().rstrip())) for _ in range(n)]
v = [[0]*m for _ in range(n)] 


def bfs(si,sj):
    q=deque()
    q.append((si,sj))
    v[si][sj] = 1
    
    x=[-1,1,0,0]
    y=[0,0,-1,1]
    while q :
        ti,tj = q.popleft()
        for i in range(4):
            di = ti + x[i]
            dj = tj + y[i]
            
            if 0<=di<n and 0<=dj<m and v[di][dj] == 0 and arr[di][dj] == 1:
                q.append((di,dj))
                v[di][dj] = 1
                arr[di][dj] = arr[ti][tj] + 1

bfs(0,0)
print(arr[n-1][m-1])
