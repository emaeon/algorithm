import sys

input=sys.stdin.readline

lst='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
N,B=map(int,input().split())

result=''
while N :
    a = N%B 
    result += lst[a]
    # print(a)
    N = N//B
    
print(result[::-1])