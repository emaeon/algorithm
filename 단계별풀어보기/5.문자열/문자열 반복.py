import sys

input=sys.stdin.readline

t=int(input().rstrip())


for _ in range(t):
    r,s=map(str,input().split())
    string=''
    for i in s:
        string+=int(r)*str(i)
    print(string)