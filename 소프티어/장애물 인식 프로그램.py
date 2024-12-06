import sys
from collections import deque

input = sys.stdin.readline
n=int(input().rstrip())

map = [list(map(int,input().rstrip())) for _ in range(n)]
v = [[0]*n for _ in range(n)]

def bfs(si,sj):
    q = deque()
    q.append((si,sj))
    v[si][sj] = 1

    x = [-1,1,0,0]
    y = [0,0,-1,1]

    temp = 1
    while q:
        ti,tj = q.popleft()
        for i in range(4):
            di = ti+x[i]
            dj = tj+y[i]

            if (0<=di<n) and (0<=dj<n) and v[di][dj]==0 and map[di][dj]==1:
                q.append((di,dj))
                v[di][dj] = 1
                temp += 1
    return temp

cnt = 0
lst = []
for i in range(n):
    for j in range(n):
        if v[i][j] == 0 and  map[i][j] == 1:
            block = bfs(i,j)
            lst.append(block)
            cnt += 1
lst.sort()
print(cnt)
print(*lst, sep='\n')
