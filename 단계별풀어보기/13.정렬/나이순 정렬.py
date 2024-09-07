import sys

input = sys.stdin.readline

n = int(input().rstrip())

lst=[]
for _ in range(n):
    a,b = map(str,input().split())
    
    lst.append([a,b,_])
    
lst.sort(key = lambda x : (int(x[0]), int(x[2])))

for x, y, z in lst:
    print(x, y)

