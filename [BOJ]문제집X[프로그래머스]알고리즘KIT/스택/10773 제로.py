import sys
# from collections import deque
input = sys.stdin.readline

k = int(input().rstrip())

lst=[]
for _ in range(k):
    temp = int(input().rstrip())
    
    if temp == 0 :
        lst.pop()
    else :
        lst.append(temp)    

print(sum(lst))