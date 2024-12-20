import sys
input = sys.stdin.readline

t = int(input().rstrip())


for _ in range(t):
    a,b = map(int,input().split())
    temp = a+b
    print(f'Case #{_+1}:', temp)