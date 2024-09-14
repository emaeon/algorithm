import sys

input = sys.stdin.readline

n = int(input().rstrip())
arr = [list(map(int,input().split()))for _ in range(n)]
dp = [[0]*n for _ in range(n)]
dp[0][0] = 1 #이거 해줘야함
def answer():
    for i in range(n):
        for j in range(n):
            jump = arr[i][j]
            #이동 가능한 거리 0 넘어가면 X
            #또는 dp가 0이라는 것은 현재 위치에 도달할 수 없음을 의미
            if jump == 0 or dp[i][j] == 0 :#여기서 틀림
                continue
            #if 0<(j+jump)<=n and 0<(i+jump)<=n :# 나눠서 해야함
                #if dp[i][j+jump] == 0 and dp[i+jump][j]==0 : #이건 없어도됨
                    #dp[i][j+jump] = 1 여기서 틀림
            if j+jump < n : #아래 이동 시, 게임판 안벗어나면 경우의 수 추가
                dp[i][j+jump] += dp[i][j]
            if i + jump < n : #위로 이동 시, 게임판 안벗어 나면 경우의 수 추가
                dp[i+jump][j] += dp[i][j]
    print(dp)
    return dp[-1][-1] #가장 마지막인 (n,n) 좌표의 경우의수 return
                
print(answer())
        
        
    

# import sys

# input = sys.stdin.readline

# n = int(input().rstrip())
# arr = [list(map(int,input().split()))for _ in range(n)]
# dp = [[0]*n for _ in range(n)]


# for i in range(n):
#     for j in range(n):
#         jump = arr[i][j]
#         if 0<(j+jump)<=n and 0<(i+jump)<=n :
#             if dp[i][j+jump] == 0 and dp[i+jump][j]==0 :
#                 dp[i][j+jump] = 1
#                 dp[i+jump][j] = 1
# print(dp)
        
        
    
