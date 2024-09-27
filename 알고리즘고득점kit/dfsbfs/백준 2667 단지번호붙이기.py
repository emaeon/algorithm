import sys
from collections import deque

input = sys.stdin.readline
n = int(input().rstrip())

arr = []
for _ in range(n) :
    temp = list(map(int,input().rstrip()))
    arr.append(temp)

v = [[0]* n for _ in range(n)]    
def bfs (si,sj) :
    q = deque()
    q.append((si,sj))
    v[si][sj] = 1
    cnt = 0
    while q :
        ti,tj = q.popleft()
        dx = [-1,1,0,0]
        dy = [0,0,-1,1]
        for idx in range(4) :
            ni = ti + dx[idx]
            nj = tj + dy[idx]
            
            if (0<= ni < n) and (0<= nj < n) and(v[ni][nj]==0) and(arr[ni][nj] != 0):
                q.append((ni,nj))
                v[ni][nj] = 1
                cnt+= 1
    return cnt

result = []
for i in range(n):
    for j in range(n) :
        if (arr[i][j]!=0) and(v[i][j]==0) :
            c = bfs(i,j)
            result.append(c)

result.sort()
print(len(result))
print(*result, sep='\n')
            