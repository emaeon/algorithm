import sys

input = sys.stdin.readline

n, m = map(int, input().split())

lst = list(map(int,input().split()))
lst = sorted(lst)

result=[]
visited = [False]*n

def back():
    if len(result) == m :
        print(*result)
        return
    temp = 0 
    for i in range(n) :
        if temp != lst[i] and not visited[i]:
        
            visited[i] = True
            result.append(lst[i])
            temp = lst[i]
            back()
            visited[i] = False
            result.pop()


back()