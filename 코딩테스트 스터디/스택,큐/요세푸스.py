from collections import deque
import sys

queue = deque()
input = sys.stdin.readline
n,k = map(int, input().split())

queue = deque([i+1 for i in range(n)])

result=[]
while queue : #큐 안에 사람들 모두 사라질 때까지 반복
    for _ in range(k-1): #K번째 사람전까지
        queue.append(queue.popleft())  #맨 앞에 있던 사람을 맨 뒤로 옮기기
        
    result.append(queue.popleft()) #K번째 사람 큐에서 제거하고 result에 그 사람 넣기

print('<',end='')
print(*result, sep=', ', end ='')
print('>',end='')