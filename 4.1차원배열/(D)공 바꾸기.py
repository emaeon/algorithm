import sys

input = sys.stdin.readline

n,m=map(int,input().split())

basket = [i+1 for i in range(n)]

for _ in range(m):
    i, j = map(int, input().split()) #1,2
    
    a=basket[i-1] #basket리스트의 1번쨰값
    b=basket[j-1] #basket리스트의 2번쨰값
    
    basket[i-1]=b #basket리스트의 1번쨰값=basket리스트의 2번쨰값
    basket[j-1]=a #basket리스트의 2번쨰값=basket리스트의 1번쨰값
    
    
    
print(*basket)


