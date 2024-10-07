import sys

input = sys.stdin.readline

n,m= map(int,input().split())
arr = []
for _ in range(n):
    a = list(map(int,input().rstrip()))
    arr.append(a)
    

v = [[0]*5 for _ in range(4)]


x = [-1,1,0,0]
y = [0,0,-1,1]

def bfs(si,sj):
    q=[]
    q.append((si,sj))
    v[si][sj] = 1
    
    while q :
        ti,tj = q.pop(0)
        for i in range(4):
            di = ti+x[i]
            dj = tj+y[i]
            if 0 <= di < n and 0 <= dj < m and v[di][dj] == 0 and arr[di][dj] == 0 :
                q.append((di,dj))
                v[di][dj] = 1
        
        
cnt = 0
for i in range(4):
    for j in range(5) :
        if v[i][j] == 0 and arr[i][j]==0:
            bfs(i,j)
            cnt += 1            

print(cnt)