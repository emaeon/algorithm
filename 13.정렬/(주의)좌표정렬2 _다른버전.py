import sys

input = sys.stdin.readline

n=int(input().rstrip())

lst=[]
for i in range(n):
    temp = list(map(int,input().split()))
    lst.append(temp)
    
lst.sort(key=lambda x:(x[1],x[0]))

for i in lst:
    print(i[0],i[1])