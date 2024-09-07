import sys

input=sys.stdin.readline

t=int(input().rstrip())
remain=[25,10,5,1]


for _ in range(t):
    price=int(input().rstrip())    
    temp_lst=[]
    for i in remain:
        temp_lst.append(price//i)
        price = price%i
    print(*temp_lst)