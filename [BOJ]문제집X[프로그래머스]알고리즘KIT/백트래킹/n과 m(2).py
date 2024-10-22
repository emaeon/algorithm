import sys
input = sys.stdin.readline

# def dfs(n,lst) :
#     if n>N: #종료조건 : n관련
#         if len(lst) == M: #M개짜리 수열 -> 정답처리
#             ans.append(lst)
#         return
#
#     dfs(n+1,lst+[n]) #선택하는 경우
#     dfs(n+1,lst) #선택하지 않은 경우

def dfs(n,s,lst) :
    if n == M :
        ans.append(lst)
        return

    for i in range(s,N+1):
        dfs(n+1,i+1,lst + [i])

N,M = map(int,input().split())
ans=[]
# dfs(1,[]) #이진트리
dfs(0, 1,[]) #멀티트리
for i in ans :
    print(*i)