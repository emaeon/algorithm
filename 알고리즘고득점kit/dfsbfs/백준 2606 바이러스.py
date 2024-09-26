import sys
input = sys.stdin.readline

n = int(input().rstrip())
line = int(input().rstrip())

arr = [[] for a in range(n+1)]

for _ in range(line):
    x, y = map(int,input().split())
    arr[x].append(y)
    arr[y].append(x)
    
v = [0 for a in range(n+1)]

def bfs(c):
    q=[]
    q.append(c)
    v[c] = 1
    cnt = 0
    
    while q :    
        t = q.pop(0)
        
        cnt += 1
        
        for j in arr[t]:
                
            if not v[j] :
                q.append(j)
                v[j] = 1
    return v

result = sum(bfs(1)) -1

print(result)

    
    
