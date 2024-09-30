import sys
from collections import deque
input = sys.stdin.readline

k,m = map(int, input().split()) #탐사 횟수, 유물조각 개수
arr = [list(map(int,input().split())) for _ in range(5)]
lst = list(map(int,input().split()))
ans = []

#1. rotate 함수
def rotate(arr, si, sj) :
    narr = [x[:] for x in arr]
    for i in range(3) :
        for j in range(3) :
            narr[si+i][sj+j] = arr[si+3-j-1][sj+i]
    return narr
#2.bfs
def bfs(arr, v, si, sj, clr) :
    q = deque()
    q.append((si,sj))
    cnt = 0
    sset = set() #?

    v[si][sj] = 1
    sset.add((si,sj))
    cnt += 1

    while q :
        ci,cj = q.popleft()
        # 4방향, 미방문, 조건(같은값)
        for di, dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni,nj = ci+di, cj+dj
            if 0<= ni <5 and 0<= nj <5 and v[ni][nj] == 0 and arr[ci][cj] == arr[ni][nj] :
                q.append((ni,nj))
                v[ni][nj] = 1
                sset.add((ni,nj)) #?
                cnt += 1

    if cnt >= 3 : #유물이 있고, 탐사진행? 연쇄획득?
        if clr == 1:
            for i,j in sset : #다시 초기화
                arr[i][j] = 0
        return cnt

    else:
        return 0

def count_clear(arr, clr) :
    v = [[0]*5 for _ in range(5)]

    cnt = 0
    for i in range(5):
        for j in range(5) : #미방문인 경우 fill
            if v[i][j] == 0 :
                t = bfs(arr, v, i, j, clr)
                cnt += t
    return cnt

for _ in range(k) :
    #[1] 탐사진행
    mx_cnt = 0

    for rot in range(1,4) : # 회전수 / 열 / 행
        for sj in range(0,3) :
            for si in range(0,3) :

                #rotate
                narr = [x[:] for x in arr]
                for _ in range(rot):
                    narr = rotate(narr, si, sj)

                # 유물개수 확인 및 갱신
                t = count_clear(narr, 0)
                if mx_cnt < t :
                    mx_cnt = t
                    marr = narr

    #유물 없는 경우 즉시 종료
    if mx_cnt == 0 :
        break

    #유물 있는 경우 연쇄 획득
    #[2]
    cnt = 0
    arr=marr

    while True :
        t= count_clear(arr, 1)
        if t==0 :
            break #연쇄획득 종료

        cnt += t #획득한 유물 개수 누적

        # arr의 0값인 부분 리스트에서 순서대로 추가 #열 +, 행 - 순으로
        for j in range(5) :
            for i in range(4,-1,-1) :
                if arr[i][j] == 0 :
                    arr[i][j] = lst.pop(0)
    ans.append(cnt) #턴 당 유물 개수

print(*ans)

