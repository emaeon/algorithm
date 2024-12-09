import sys
from collections import deque
input = sys.stdin.readline

n,m=map(int,input().split())

array = [list(map(int,input().split())) for _ in range(n)]
v = [[0]*m for _ in range(n)]

## bfs
def bfs(si,sj):
    q = deque()
    q.append((si,sj)) #시작할 초기 좌표
    v[si][sj] = 1 #초기 좌표 방문처리

    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    cnt = 1 #while 문 안에 있으면 안됨. 탐색할 때마다 0됨
    while q : #방문할 곳 없을 때 까지
        ti,tj = q.popleft()
        for i in range(4):
            di = ti + dx[i]
            dj = tj + dy[i]
            if (0<=di<n) and (0<=dj<m) :
                if (v[di][dj]==0) and (array[di][dj]==1):
                    q.append((di,dj))
                    v[di][dj] = 1
                    cnt += 1
    return cnt

max_count=0
picture_cnt=0
## array에서 1이고, v에서 방문하지 않았을 때, bfs하면서 max_count보다 현재 count가 더 높으면 대체(가장넓은넓이), bfs한번 하면 카운트 하기(그림수)
for i in range(n):
    for j in range(m):
        if (v[i][j]==0) and (array[i][j]==1):
            temp = bfs(i,j)
            if temp > max_count :
                max_count = temp
            picture_cnt+=1

print(picture_cnt, max_count, sep='\n')