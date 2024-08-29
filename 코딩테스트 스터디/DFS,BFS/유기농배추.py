import sys
from collections import deque
input = sys.stdin.readline

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(graph,a,b):
    q = deque()
    q.append((a,b))
    graph[a][b] = 0

    while q :
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= m or ny < 0 or ny >= n :
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                q.append((nx,ny))


t = int(input().rstrip())
            
for _ in range(t):
    m, n, k = map(int,input().split())
    
    graph = [[0]*(n) for _ in range(m)]

    for i in range(k):
        a,b = map(int,input().split())
        graph[a][b] = 1
    
    count = 0        
    for j in range(m):
        for k in range(n):
            if graph[j][k] == 1:
                bfs(graph,j,k)
                count +=1
            
    print(count)