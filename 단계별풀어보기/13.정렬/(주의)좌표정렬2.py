import sys

input = sys.stdin.readline

n= int(input().rstrip())
lst = []
for _ in range(n):
    a= list(map(int, input().split()))
    lst.append(a)
    
    
lst2 = []

for i in range(len(lst)):
    a = lst[i][1]
    b = lst[i][0]
    lst2.append([a,b])
    

lst2.sort()

lst3 = []
for j in range(len(lst)):
    c = lst2[j][1]
    d = lst2[j][0]
    lst3.append([c,d])
    
# print(lst2)
for _ in lst3:
      
    print(*_, sep=" ")
