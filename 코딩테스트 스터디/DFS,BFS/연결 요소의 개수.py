import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

#그래프
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m) :
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

#visitied
visited = [False] *(n+1)

#dfs
def dfs(v):
    visited[v]=True
    # print(v, end = ' ')
    
    for i in graph[v]:
        if not visited[i]:
            dfs(i)
            
            
count = 0

for i in range(1, n+1):
    if not visited[i]:
        dfs(i)
        count+=1
#dfs 실행

print(count)