import sys
input=sys.stdin.readline

H,M=map(int,input().split())
#H가 0보다 작고 M<45면
#H=23, M=60-45+M

#M-45가 0보다 작으면 H-1
#M=40 , 55(60-45 +40)

if H==0 and M<45 :
    A=23
    B=60-45+M
    print(A,B, end=" ")
elif  M<45 :
    A=H-1
    B=60-45+M
    print(A,B, end=" ")
else:
    A=H
    B=M-45
    print(A,B)