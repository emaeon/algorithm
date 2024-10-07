def solution(progresses, speeds):
    answer = []
    cnt = 0
    
    while progresses:
        
        for i in range(len(progresses)):            
            progresses[i] += speeds[i]        
        
        if progresses[0] >= 100 :
            
            while True :
                
                if len(progresses) > 0 :
                    
                    if progresses[0] >= 100 :
                        progresses.pop(0)
                        speeds.pop(0)
                        cnt += 1

                    else : break
                else : break
            
            answer.append(cnt)
            cnt = 0
            
    return answer