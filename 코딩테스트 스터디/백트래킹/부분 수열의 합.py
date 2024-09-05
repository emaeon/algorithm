import sys

input = sys.stdin.readline

n, s = map(int, input().split())
#수열의 모든 경우의 수를 가지고 합이 S인 경우 세기
num = list(map(int,input().split()))

cnt = 0
ans = []

def back(start):
    global cnt
    if sum(ans) == s and len(ans) > 0:
        cnt +=1
    
    for i in range(start, n):
        ans.append(num[i])
        back(i+1)
        ans.pop()
back(0)
print(cnt)
        