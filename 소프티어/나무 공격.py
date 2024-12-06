import sys
input = sys.stdin.readline

n,m = map(int,input().split())

lst = []
for _ in range(n):
    temp = list(map(int,input().split()))
    lst.append(temp)

min_a,max_a = map(int,input().split())
min_b,max_b = map(int,input().split())

for i, l in enumerate(lst): #행
    if i+1 not in range(min_a,max_a+1):
        pass
    else:
        for j in range(len(l)): #열
            if l[j] == 1:
                lst[i][j] = 0
                break

for i, l in enumerate(lst): #행
    if i+1 not in range(min_b,max_b+1):
        pass
    else:
        for j in range(len(l)): #열
            if l[j] == 1:
                lst[i][j] = 0
                break
cnt = 0
for a in lst:
    for b in a :
        if b == 1 :
            cnt += 1

print(cnt)