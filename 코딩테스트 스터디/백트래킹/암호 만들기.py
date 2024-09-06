import sys

L,C= map(int,input().split())

lst = list(map(str,input().split()))
lst.sort()

result = []
visited = [False]*C

def back():
    
    if len(result) ==  L :
        print(*result, sep='')
        return
    temp = ''
    for i in range(C) :
        if temp != lst[i] and not visited[i]: 
            
            visited[i] = True
            result.append(lst[i])
            temp = lst[i]
            back()
            visited[i]= False
            result.pop()
            
back()        