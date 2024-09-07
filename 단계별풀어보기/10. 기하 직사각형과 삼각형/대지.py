import sys

input=sys.stdin.readline

# 규칙
# x에서 제일 큰 수 - 제일 작은 수
# y에서 제일 큰 수 - 제일 작은 수
# 두 값을 곱 

n = int(input().rstrip())

lstx=[]
lsty=[]
for _ in range(n):
    x,y = map(int,input().split())
    lstx.append(x)
    lsty.append(y)
    
if len(lstx) == 1:
    print(0)
    
else:
    w = max(lstx)-min(lstx)
    h = max(lsty)-min(lsty)

    print(w*h)
    