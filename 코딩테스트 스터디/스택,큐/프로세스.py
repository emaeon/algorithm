from collections import deque

def solution(priorities, location):
    answer = []
    queue = deque((_,i) for _,i in enumerate(priorities))
    
    while queue :
        
        word = queue.popleft()
        if any(word[1]<q[1] for q in queue):
            queue.append(word)
        else:
            answer.append(word)
    
    for i in answer :
        if i[0] == location :
            return answer.index(i) +1