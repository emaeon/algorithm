import sys

input = sys.stdin.readline

n = int(input().rstrip())

#5키로로 나누기, 3키로로 뺴기

cnt = 0
while True:
    
    if n == 0 :
        print(cnt)
        break
    elif n==4 or n<3 :
        print(-1)
        break
    
    if n % 5 == 0 :
        cnt += n//5
        print(cnt)
        break
    
    else:
        n -= 3
        cnt += 1
        