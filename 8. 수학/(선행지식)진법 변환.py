import sys

input = sys.stdin.readline

N,B=map(str,input().split())
alpha_lst=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
num_lst=[i for i in range(10,36)]

result=0
for i in range(len(N)):
    
    if N[::-1][i] not in alpha_lst :
        result+=int(N[::-1][i])*(int(B)**i)
    else:
        result+=(num_lst[alpha_lst.index(N[::-1][i])])*(int(B)**i)

print(result)
    

# print((35*(36**4))+(35*(36**3))+(35*(36**2))+(35*(36**1))+(35*(36**0)))
