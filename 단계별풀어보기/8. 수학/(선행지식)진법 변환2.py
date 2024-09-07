import sys

input=sys.stdin.readline

lst='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
N,B=map(int,input().split())

result=''
while N :
    a = N%B 
    result += lst[a]
    # print('대상:',N,'나머지:',a)
    N = N//B
    
print(result[::-1])