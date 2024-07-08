import sys

input = sys.stdin.readline

n= int(input().rstrip())

lst  =  list(map(int,input().split()))
pool = list(set(lst))

pool.sort()

p_dict={}

for i in range(len(pool)):
    p_dict[pool[i]] = i
    
for j in lst:
    print(p_dict[j], end=' ')