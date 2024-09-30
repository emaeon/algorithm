import sys
input = sys.stdin.readline

n = int(input().rstrip())

dp = [0] * (n+1)

for i in range(2,n+1):
    temp = []
    
    if (i%3) == 0 :
        temp.append(dp[i//3] + 1)
        
    if i%2 == 0 :
        temp.append(dp[i//2] + 1 )
            
    temp.append(dp[i-1] + 1)
    dp[i] = min(temp)

print(dp[n])