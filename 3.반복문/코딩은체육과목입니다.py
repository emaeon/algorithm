import sys

input=sys.stdin.readline

N=int(input())

A = N//4
# name = A*str('long')

a=''
for _ in range(A):
   a += str('long ')

print(a+'int',end="") #,는 자동으로 공백이 생김, 따라서 +로
