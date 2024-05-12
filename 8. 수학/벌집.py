import sys

input=sys.stdin.readline
t=int(input().rstrip())
# 1 -> 1(n=1)
# 2 -> 2 3 4 5 6 7 (n=6)
# 3 -> 8 9 10 11 12 13 14 15 16 17 18 19 (n=12)
# 4 -> 20 ~ 37 (n=18)
# 6*1 6*2 6*3 6*4
# 6n+1  

while True:
    n=0
    lst = [i for i in range(0,6*n+2)]
    
    if t in lst :
        print(n)
        break
    else :
        n+=1
    
#range(1+6*0+6*1,1+6*1+6*2)
    