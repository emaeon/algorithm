import sys
from collections import deque
input = sys.stdin.readline

n = int(input().rstrip())
a,b = map(int,input().split())
m = int(input().rstrip())

arr = [[] for _ in range(n+1)]

for _ in range(m):
    x,y = map(int,input().split()) 
    arr[x].append(y) 
    arr[y].append(x)

v = [0]*(n+1)

def BFS(start) :
    q = deque()
    q.append(start)
    v[start] = 1
    
    while q :
        
        t = q.popleft()        
        
        for i in arr[t] :
            if v[i] == 0 :
                q.append(i)
                v[i] = v[t] + 1
    return v

v = BFS(a)

print(v[b]-1)