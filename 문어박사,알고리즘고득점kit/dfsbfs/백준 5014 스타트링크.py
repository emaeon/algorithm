import sys

input = sys.stdin.readline

f,s,g,u,d = map(int,input().split())

v=[0]*(f+1)

def bfs(c):
    q=[]
    q.append(c)
    v[c] = 1
    while q :
        t = q.pop(0)
        if t == g : return v[g] -1
        
        for i in [u,-d]:
            dc = t+i
            if (0<dc<len(v)) and v[dc] == 0 :
                v[dc] = v[t] + 1
                q.append(dc)
    return 'use the stairs'

result = bfs(s)
print(result)