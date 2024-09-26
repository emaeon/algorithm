import sys

input = sys.stdin.readline

n, m = map(int,input().split())

arr = []
for i in range(n) :
    a = list(map(int,input().rstrip()))
    arr.append(a)
v = [[0]*m for j in range(n)]

x,y = [-1,1,0,0],[0,0,-1,1]

def bfs(si,sj):
    q = []
    q.append((si,sj))
    v[si][sj] = 1
    
    
    while q :
        ti,tj = q.pop(0)
        
        for idx in range(4):
            di = ti + x[idx]
            dj = tj + y[idx]
            
            if (0<=di<n) and (0<=dj<m) and v[di][dj]==0 and arr[di][dj]==1:
                q.append((di,dj))
                v[di][dj] = v[ti][tj] +1
    return v[n-1][m-1]

result= bfs(0,0)
print(result)
                
        
    