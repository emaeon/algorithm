import sys
input = sys.stdin.readline
from collections import deque


#dfs
#정점개수, 간선개수, 탐색을시작할정점번호
n,m,v = map(int,input().split())
arr = [[] for i in range(n+1)]
for _ in range(m):
    a,b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)


def dfs(c) :
    #단위 
    global v, result
    visited[c] = 1
    result.append(c)
    arr[c].sort()
    
    for test in arr[c] :
        if not visited[test] :
            dfs(test)
            

def bfs(s) :
    q = deque()
    q.append(s)
    result.append(s)
    visited[s] = 1
    
    
    while q :
        temp = q.popleft()
        arr[temp].sort()
        for i in arr[temp] :    
            if not visited[i] :
                q.append(i)
                result.append(i)
                visited[i] = 1
                
        
    


visited=[0]*(n+1)
result=[]
dfs(v)
print(*result)

visited=[0]*(n+1)
result=[]
bfs(v)
print(*result)


