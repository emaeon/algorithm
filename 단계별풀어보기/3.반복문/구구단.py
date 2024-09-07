import sys
input=sys.stdin.readline

N=int((input().rstrip()))

for i in range(1,10):
    A=i*N
    print(N,'*',i,'=',A)
