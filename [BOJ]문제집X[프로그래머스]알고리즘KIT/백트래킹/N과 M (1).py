import sys

input = sys.stdin.readline

N,m = map(int,input().split())

ans = [] # 정답 리스트를 저장할 
v = [0]*(N+1)


def dfs(n,lst) :
    if n == m : #종료조건(n관련) 처리 + 정답처리
        ans.append(lst)
        return
    
    #하부단계(함수) 호출
    for j in range(1,N+1) :
        if v[j] == 0:
            v[j] = 1
            dfs(n+1, lst+[j])
            v[j] = 0

dfs(0,[])

for i in ans :
    print(*i)
        