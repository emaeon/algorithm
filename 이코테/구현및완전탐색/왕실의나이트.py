import sys
input=sys.stdin.readline

x = [-1,1,-1,1,-2,-2,2,2]
y = [2,2,-2,-2,1,-1,1,-1]
dy = ['a','b','c','d','e','f','g','h']

lst = list(input().rstrip())
temp_x=int(lst[1])
temp_y=int(dy.index(lst[0]))+1

cnt = 0
for i in range(8):
    nx = temp_x+x[i]
    ny = temp_y+y[i]
    
    if nx<1 or nx>8 or ny<1 or ny>8:
        pass
    else:
        cnt +=1
        
print(cnt)