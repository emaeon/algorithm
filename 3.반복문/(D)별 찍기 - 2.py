import sys

input = sys.stdin.readline

t=int(input().rstrip())

for i in range(1,t+1):
    print((t-i)*str(' ')+i*str('*'))