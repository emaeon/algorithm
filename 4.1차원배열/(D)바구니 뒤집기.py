import sys

input = sys.stdin.readline

n,m = map(int, input().split())

basket = [k+1 for k in range(n)]

for _ in range(m):
    i,j = map(int, input().split()) #i~j
    #1~4면 basket1 = basket4, 2 3, 3 2, 4 1
    lst=basket[i-1:j]
    basket[i-1:j]=lst[::-1]
print(*basket)
    

        
    