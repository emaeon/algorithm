import sys
input=sys.stdin.readline

X=int(input().rstrip())
N=int(input().rstrip())

price=0
for i in range(N):
    a,b=map(int,input().split())
    price+=a*b

if price==X:
    print("Yes")
else:
    print("No")