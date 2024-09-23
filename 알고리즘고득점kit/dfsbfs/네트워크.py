from collections import deque

def solution(n, computers):
    answer = 0
    
    visited = [0 for _ in range(n)]
    
    def bfs(a,visited, n,computers) :
        q = deque()
        q.append(a)
        visited[a] = 1

        while q :
            com = q.popleft()
            
            for idx in range(n):
                 if idx != com and computers[com][idx] == 1 :
                    if visited[idx] == 0 :
                        q.append(idx)
                        visited[idx] = 1
    
    for com in range(n) :
            if not visited[com] :
                bfs(com,visited,n,computers)
                answer += 1
                
    return answer