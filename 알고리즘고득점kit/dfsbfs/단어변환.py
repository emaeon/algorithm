def solution(begin, target, words):
    answer = 0
    v = [0]*(len(words))
    
    def bfs (begin,target,words,count,v) :
        q=[]
        q.append((begin,count))   

        while q :
            word, count = q.pop(0)
            if word == target :
                return count
    

            for i in range(len(words)) :
                temp = 0
                if not v[i]:
                    for j in range(len(word)):
                        if word[j]!= words[i][j]  :
                            temp +=1
                            
                    if temp == 1 :
                        q.append((words[i],count + 1))
                        v[i] = 1
        return 0
    
    answer = bfs(begin,target,words,0,v)
    return answer