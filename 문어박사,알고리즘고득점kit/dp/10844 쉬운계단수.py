import sys

input = sys.stdin.readline

n = int(input().rstrip())

dp = [[0]*12 for _ in range(n+1)]
dp[1][2:11]  = [1]*9


for i in range(2,n+1):
    for j in range(1,11):
        dp[i][j] = dp[i-1][j-1]+dp[i-1][j+1]

print(sum(dp[n])%1000000000)
        