import sys
input=sys.stdin.readline

n = int(input().rstrip())
words = list(input().rstrip())
visited = True #도달 불가능 여부

#dp선언
dp = list([1e9,not visited] for _ in range(n))
dp[0][0], dp[0][1]=0, True

'''첫칸은 B로 고정, 인덱스 1~N까지 각각 점프가능한지, 
가능한 최솟값은 어떻게 되는지 구하기'''

for i in range(1,n):
    word = words[i]    
    #블록마다 점프가 가능한 경우의 수

    check_jump = '?'
    if word =='B':
        check_jump = 'J'
    elif word == 'O':
        check_jump = 'B'
    else :
        check_jump = 'O'
    for j in range(i):
        if check_jump == words[j]:
            #j -> i로 점프        
            #뒤에 있는 블록들로 부터 해당 블록까지 점프할 때, 에너지의 최솟값
            #점프 거리의 제곱만큼 에너지 소모
            dp[i][0] = min(dp[i][0], dp[j][0] + pow(i-j, 2))#점화식
            
            if dp[i][0] != 1e9:
                dp[i][1] =True
                            
if dp[n-1][1]:
    print(dp[n-1][0])          
else:
    print(-1)














# count = 0
# d=[0]*len(word)
# for i in range(1,len(word)+1) :
#     if word[i] == 'O'and 'j' in word[i:]:
#         count += (i)*(i)
#         d[i]=word[i]
        
#     if word[i] == 'J'and 'O' in word[:i]:
#         idx = i - d.index('O')
#         count += (idx)*(idx)
#         d[i]=word[i]
        
#     if word[i] =='B' and 'J' in word[:i]:
        
    
    
        
    
        
        
    
