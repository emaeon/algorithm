import sys
from collections import deque
input = sys.stdin.readline

n = int(input().rstrip())

q = deque()
for i in range(n):
    temp = list(map(str, input().split()))
    if len(temp) == 2:
        q.append(int(temp[1]))

    elif 'pop' in temp :
        if len(q) > 0 :
            print(q.popleft())
        else :
            print(-1)

    elif 'size' in temp :
        print(len(q))

    elif 'empty' in temp :
        if len(q) >0 :
            print(0)
        else:
            print(1)
    elif 'front' in temp :
        if len(q) >0 :
            print(q[0])
        else :
            print(-1)

    elif 'back' in temp :
        if len(q) > 0:
            print(q[-1])
        else:
            print(-1)






