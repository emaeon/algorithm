# 현재 시각 A,B
# 요리에 필요한 시간 C(0~1000)
# 23시 40분에 120분이 걸릴떄? 1시 40분
#A=23, B=40, C=120
# 분: 160(B40+C120), 총 40분(B+C 160%60)
# 시: 25(A23+2), 1시(A 23 + B+C160//60)-24
# 160=B+C 

import sys
input = sys.stdin.readline

A,B=map(int,input().split())
C= int(input())

m = B+C
if m>=60 : # 0일경우도 생각해야함
    temp_m=m%60
    temp_h=m//60
    
    if (A + temp_h)>=24: # 0일경우도 생각해야함
        
        print(A+temp_h-24, temp_m, end=" ")
    elif (A + temp_h)<24:     
        print(A+temp_h, temp_m, end=" ")
        
elif m<60:
    print(A,m,end=" ")
