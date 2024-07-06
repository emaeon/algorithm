import sys

input = sys.stdin.readline

n = int(input().rstrip())

lst=[]
for i in range(n):
    temp = input().rstrip()
    lst.append([len(temp),temp])

lst.sort(key = lambda x : (x[0], x[1]))

lst2 =[]

for i in lst:
    
    if i[1] in lst2:
        pass
    else:
        lst2.append(i[1])
        
for j in lst2:
    print(j)