import sys
from collections import deque

n, m = map(int, input().split())
dx = [-1,1,0,0]
dy = [0,0,-1,1]

#그래프 생성
graph = [] #인덱스 0 접근 안하게 미리 리스트하나 넣어주기
for _ in range(n):
    graph.append(list(map(int,input().rstrip())))

def bfs(a,b):
    q=deque()
    q.append((a,b))
    while q :
        x,y = q.popleft()
    
        for j in range(4):
            nx = x + dx[j]
            ny = y + dy[j]
            if nx <0 or nx >= n or ny <0 or ny >=m :
                continue
            if graph[nx][ny] == 1 :
                q.append((nx,ny))
                graph[nx][ny] = graph[x][y] +1

    return graph[n-1][m-1]
  
print(bfs(0,0))


# for z in range(n):
#     for k in range(m):
#         if graph[z][k]== 1:
#             result.append(bfs(z,k))



                
                
                
                
            
     
    

