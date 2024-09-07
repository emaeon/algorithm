import sys

input = sys.stdin.readline

a1,a=map(int,input().split())
c=int(input().rstrip())
n0=int(input().rstrip())

for i in range(n0,101):
    if (a1*i)+a <= c*i:
        if i ==100 :
            print(1)
    else:
        print(0)
        break
