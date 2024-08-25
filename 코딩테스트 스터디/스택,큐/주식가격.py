from collections import deque
def solution(prices):
    answer = []
    queue = deque(prices)
    
    while queue :
        cnt = 0
        word = queue.popleft()
        
        for i in queue :
            cnt+=1
            if word <= i:
                pass
            else:
                break
        answer.append(cnt)
    return answer