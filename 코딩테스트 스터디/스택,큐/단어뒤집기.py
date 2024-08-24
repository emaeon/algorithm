from collections import deque
import sys

input = sys.stdin.readline

t = int(input().rstrip())

for _ in range(t):
    
    lst = []
    a = list(map(str, input().split()))
    temp = deque(a)
    
    while temp :
        word = temp.popleft()
        lst.append(word[::-1])
    
    print(*lst, sep = ' ')