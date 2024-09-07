import sys

input=sys.stdin.readline

n=int(input().rstrip())

lst=list(map(int,input().split()))

cnt = n
for i in range(n):
    if lst[i]==1:
        cnt -=1
        pass
    else:
        for j in range(2,lst[i]):
            if lst[i]%j==0:
                cnt -=1
                break
            else:
                pass
                
print(cnt)