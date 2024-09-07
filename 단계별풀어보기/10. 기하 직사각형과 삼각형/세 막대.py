import sys

input = sys.stdin.readline

a,b,c = map(int,input().split())

if max(a,b,c) < a+b+c-max(a,b,c):
    print(a+b+c)

else:
    lst = [a,b,c]
    lst.remove(max(a,b,c))

    lst.append(sum(lst)-1)

    print(sum(lst))