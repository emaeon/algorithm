import sys
input = sys.stdin.readline

n, m = map(int,input().split())
tower = [0]*101

start = 1
for _ in range(n) :
    a, b = map(int,input().split())
    for i in range(start,(start + a)) :
        tower[i] = b
    start = start+a

start = 1
for _ in range(m) :
    a,b = map(int,input().split())
    for i in range(start,(start + a)) :
        if tower[i]-b > 0 :
            tower[i] = 0
        else :
            tower[i] = b-tower[i]
    start = start+a
print(max(tower))