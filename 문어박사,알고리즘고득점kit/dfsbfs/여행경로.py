def solution(tickets):
    answer = []
    v= [0] * len(tickets)
    
    def dfs(airport, path) :
        
        if len(tickets)+1 == len(path) : #잘 이해가 안감 왜 +1?
            answer.append(path) 
            return

        for idx, value in enumerate(tickets) :
            if value[0] == airport and v[idx] == 0 : #출발공항인데 방문 안했다면
                v[idx] = 1 #방문처리
                dfs(value[1], path+[value[1]]) #도착공항을 출발공항으로 지정, 이해안가는점 path+[]로하지 왜
                v[idx] = 0 #중복 방문을 위해 다시 방문안한것으로 처리
                    
    dfs('ICN',['ICN'])
    
    answer.sort()
    
    
    return answer[0]