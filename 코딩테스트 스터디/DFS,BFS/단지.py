import sys
from collections import deque


def dfs(idx):
    global visited
    visited[idx] = True
    print(idx, end=' ')
    
    for i in range(1, n+1):
        if not visited[i] and graph[idx][i]:
            dfs(i)

def bfs():
    global queue, visited
    while queue :
        cur = queue.popleft()
        visited[cur] = True
        print(cur, end=' ')
        
        for i in range(1, n+1):
            if not visited[i] and graph[cur][i]:
                visited[i] = True
                queue.append(i)
            
    
#0. input 받기
input = sys.stdin.readline
n, m, v = map(int, input().split())


#1. graph 및 visited 배열 선언
graph=[[False]*(n+1) for _ in range(n+1)]
dd
for _ in range(m):
    a, b = map(int,input().split())
    graph[a][b] = True
    graph[b][a] = True
# print(graph)
visited= [False]*(n+1)

dfs(v)
print()

visited = [False]*(n+1)
queue = deque([v])
bfs()