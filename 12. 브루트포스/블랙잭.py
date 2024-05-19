import sys
import itertools 
input = sys.stdin.readline

n, m = map(int,input().split())

lst = list(map(int,input().split()))

templst=[]
for i in itertools.combinations(lst,3):
    
    templst.append(sum(i))
    
result=[]
for i in templst:
    if i <=m :
        result.append(i)


print(max(result))