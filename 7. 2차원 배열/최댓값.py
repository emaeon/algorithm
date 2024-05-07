import sys

input = sys.stdin.readline

#9X9 행렬

lst =[]

maxnum=0
#모두 저장
for _ in range(9):
    temp=list(map(int,input().split()))
    lst.append(temp)
    if max(temp) >= maxnum:
        maxnum = max(temp)
    else:
        pass

for i in range(len(lst)):
    for j in range(len(lst[i])):
        if lst[i][j]==maxnum:
            print(maxnum)
            print(i+1,j+1)
    