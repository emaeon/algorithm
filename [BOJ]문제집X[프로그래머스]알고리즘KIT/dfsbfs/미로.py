import sys
from collections import deque
input = sys.stdin.readline

n,m=map(int,input().split())

lst=[ list(map(int,input().rstrip())) for _ in range(n)]
v = [[0]*m for _ in range(n)]
x = [-1,1,0,0]
y = [0,0,-1,1]

def bfs(si,sj):
    q= deque()
    q.append((si,sj))
    v[si][sj] = 1
    
    while q:
        ti,tj=q.popleft()

        for i in range(4):
            di = ti+x[i]
            dj = tj+y[i]
            
            if 0<=di<n and 0<=dj<m and v[di][dj] ==0 and lst[di][dj] == 1 :
                q.append((di,dj))
                v[di][dj]=v[ti][tj]+1

    return v[n-1][m-1]

result=bfs(0,0)
print(result)
#
# for i in range(n):
#     for j in range(m):
#         if v[i][j]==0 and lst[i][j] == 1:
#             bfs(i,j)

# print(v[n-1][m-1])