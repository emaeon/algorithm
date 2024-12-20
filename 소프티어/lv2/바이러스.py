import sys
input = sys.stdin.readline

#바이러스 2, 증가율 3, 총 시간 2

k,p,n = map(int,input().split())

for i in range(n):
    k *= p
    k %= 1000000007

print(k)