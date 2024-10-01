import sys
from collections import deque

input = sys.stdin.readline

r,c,k = map(int,input().split()) #행, 열, 골렘 수

unit = [list(map(int,input().split())) for _ in range(k)] #골렘

arr = [[1]+[0]*c+[1] for _ in range(r+3)] + [[1]*(c+2)]
exit_set = set()
#

di = [-1, 0, 1, 0]
dj = [0, 1, 0 ,-1]


#bfs
def bfs(si,sj):
    q = deque()
    v = [[0] + [0] * c + [0] for _ in range(r + 3)] + [[0] * (c + 2)]
    mx_i = 0

    q.append((si,sj))
    v[si][sj] = 1

    while q :
        ci,cj =q.popleft()

        mx_i = max(mx_i,ci)

        for di, dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni,nj = ci+di,cj+dj
            if not v[ni][nj] and ((arr[ci][cj] == arr[ni][nj]) or ((ci,cj) in exit_set and arr[ni][nj]>1)) :
                q.append((ni,nj))
                v[ni][nj] = 1
    return mx_i-2

ans = 0
num = 2
for cj, dr in unit : #열, 탈출좌표
    ci = 1 #행
    while True : # 골렘 움직이기
        if (arr[ci+1][cj-1] + arr[ci+2][cj] + arr[ci+1][cj+1]) == 0 :
            ci += 1

        elif (arr[ci-1][cj-1] + arr[ci][cj-2]+arr[ci+1][cj-2]+arr[ci+1][cj-1]+arr[ci+2][cj-1]) == 0 :
            ci += 1
            cj -= 1
            dr = (dr-1)%4

        elif (arr[ci-1][cj+1] + arr[ci][cj+2]+arr[ci+1][cj+2]+arr[ci+1][cj+1]+arr[ci+2][cj+1]) == 0 :
            ci += 1
            cj += 1
            dr = (dr+1)%4
        else :
            break

    if ci < 4: #움직이는 도중 최대로 내려갔음에도 좌표 밖에 있는 경우
        arr = [[1]+[0]*c+[1] for _ in range(r+3)] + [[1]*(c+2)]
        exit_set = set()
        num= 2

    else :
        arr[ci+1][cj] = arr[ci-1][cj] = num #위 아래
        arr[ci][cj-1:cj+2] = [num] * 3 #행 그대로, 좌 가운데 우
        num += 1
        #출구
        exit_set.add((ci + di[dr], cj +dj[dr]))

        ans += bfs(ci,cj)


print(ans)
