import sys

input = sys.stdin.readline

a = int(input().rstrip())
b = int(input().rstrip())
c = int(input().rstrip())

if a == 60 and b == 60 and c ==60 :
    print('Equilateral')
elif (a+b+c ==180) and ((a== b) or(a== c)or(b== c)):
    print('Isosceles')
elif (a+b+c ==180) and ((a!= b) and (a != c) and (b != c)):
    print('Scalene')
elif a+b+c != 180:
    print('Error')