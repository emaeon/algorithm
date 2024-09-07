import sys

input = sys.stdin.readline

while True:
    a,b,c=map(int,input().split())
    lst=[a,b,c]
    lst.remove(max(lst))

    if a==0 and b==0 and c==0:
        break
    
    if max(a,b,c) >= sum(lst):
        print('Invalid')
        
    elif a == b and b==c and a==c:
        print('Equilateral')
    elif (a==b and a != c) or (b==c and a != c) or (a==c and b != c):
        print('Isosceles')
    elif (a != b) and (a != c) and (b != c):
        print('Scalene')