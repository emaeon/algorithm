import sys

input = sys.stdin.readline

n, x = map(int, input().split())

lst=list(map(int,input().split()))

answer=[]
for i in range(n):  
    if lst[i] < x:
        answer.append(lst[i])
        
print(*answer) # 요소 한줄에 한번에 출력
        