#같은 눈 3개 : 10000 + (같은 눈)*1000
#같은 눈 2개 : 1000 + (같은 눈)*100
#모두 다른 눈 : (가장큰 눈)*100

import sys

input=sys.stdin.readline

a,b,c,=map(int,input().split())

if a==b==c:
    price=10000 + a*1000
    print(price)
    
elif (a==b and a!=c):
    price=1000+a*100
    print(price)
elif (a==c and a!=b):
    price=1000+a*100
    print(price)
elif (b==c and a!=c):
    price=1000+b*100
    print(price)
    
else:
    max_num=max(a,b,c)
    print(max_num*100)
    