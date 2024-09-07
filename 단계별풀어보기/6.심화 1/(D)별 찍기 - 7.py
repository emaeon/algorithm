
t = int(input())

for i in range(t):
    print(' '*((t-1)-i)+'*'*(2*(i+1)-1))

for j in range(t-1,0,-1): # j : 4, 3, 2, 1
    print(' '*(t-j)+'*'*(2*j-1))