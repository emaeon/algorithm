import sys

input=sys.stdin.readline

answer=[1,1,2,2,2,8]

lst=list(map(int,input().split()))

count=[]
for i in range(len(lst)):
    count.append(answer[i]-lst[i])
    
print(*count)