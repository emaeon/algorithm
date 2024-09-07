import sys

input=sys.stdin.readline

a,b,c,d,e,f = map(int,input().split())

for i in range(-999,1000):
    for j in range(-999,1000):
        if ((a*i)+(b*j) == c) and ((d*i)+(e*j) == f):
            print(i, j)
            break


# y=0
# for j in range(-999,1000):
#     if (b-(a*e/d))*j == c-(f*(a/d)):
#         y=j
#         break
# try:
#     x=(c-(b*y))/a
# except:
#     x=(f-(e*y))/d

# print(int(x),y)