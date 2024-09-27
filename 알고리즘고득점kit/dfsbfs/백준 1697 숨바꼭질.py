import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())
v=[0]*(100001)

def bfs(c):
    q=deque()
    q.append(c)
    v[c] = 1
    while q :
        t = q.popleft()
        dx = [1,-1,2]
        if t == k : return v[k] - 1
        for idx in dx :
            if idx == 2:
                nx = t * idx
            else :
                nx = t + idx
            if (0<=nx<len(v)) and (v[nx]==0) :
                q.append(nx)
                v[nx] = v[t] + 1

ans = bfs(n)
print(ans)