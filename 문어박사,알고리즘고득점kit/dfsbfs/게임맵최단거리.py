from collections import deque

def solution(maps):
    answer = 0
    #visited 선언 
    n,m = len(maps), len(maps[0])
    visited = [[0]*(m) for _ in range(n)]

    #BFS 함수
    def BFS(maps, visited, si,sj,ei,ej) :
        q = deque()
        n,m = len(maps), len(maps[0])
        
        q.append((si,sj))
        visited[si][sj] = 1
        
        
        x,y = [-1,1,0,0],[0,0,-1,1]
        cnt = 0
        result=[]
        while q :
            ri,rj = q.popleft()
            for idx in range(4) :
                di = ri + x[idx]
                dj = rj + y[idx]
                
                if(0<=di<n) and (0<=dj<m) :
                    if not visited[di][dj] and maps[di][dj] == 1 :
                        
                        q.append((di,dj)) 
                        visited[di][dj] = visited[ri][rj] + 1
                        
        if visited[n-1][m-1] == 0 : visited[n-1][m-1] = -1

        return visited[n-1][m-1]
    
    answer = BFS(maps, visited, 0, 0, n-1,m-1)
    return answer