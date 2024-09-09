n,m= map(int,input().split())
 
s = []
 
def dfs():
    if len(s)==m: #m=2
        print(' '.join(map(str,s)))
        return
    
    for i in range(1,n+1):  #[1, 1] -> == m과 길이 -> [1]-> [1,2] 
        s.append(i)
        dfs()
        s.pop()#길이 같아지면 return하고 실행되니 빠짐
dfs()