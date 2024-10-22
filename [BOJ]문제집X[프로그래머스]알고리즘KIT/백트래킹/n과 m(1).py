'''
가능한 모든 경우를 실행해 정답을 찾는 형태(트리형태로 펼쳐서)

(첫번째 숫자는 단계가 진행되는 형태)

n:선택된 숫자 개수(길이), 종료조건과 관련된 것으로 n을 설정
길이 m짜리 수열
* 일반화를 시킬 수 있어야 함
중복 체크 (visited, if, 함수 등)

n이 M이 되면 종료(정답처리)

하나의 함수만 짜면(dfs(n, ..) )됨

dfs(n,lst,...)
1. 종료 조건 if n==m: ans.append(lst) return
2. 하부 함수 호출
    for j(1,n+1):
        if v[j] == 0 :
            v[j]=1
            dfs(n+1,lst+[j])
            v[j] = 0
'''

import sys
input = sys.stdin.readline

def dfs(n, lst):
    #종료조건(n에 관련) 처리, 정답처리
    if n == M: #M개의 수열 완성
        ans.append(lst)
        return

    #하부 단계(함수) 호출
    for i in range(1,N+1) :
        if v[i] == 0 : #선택하지 않은 숫자인 경우 추가
            v[i] = 1
            dfs(n+1, lst+[i])
            v[i] = 0


N,M = map(int,input().split())
ans = [] #정답 리스트를 저장할 리스트
v = [0]*(N+1) #중복확인을 위한 visited[]

dfs(0,[])
for i in ans :
    print(*i)