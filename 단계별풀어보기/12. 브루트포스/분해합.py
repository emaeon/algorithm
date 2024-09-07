import sys

input = sys.stdin.readline

a = int(input().rstrip())

lst = []

for i in range(a) :
    temp = i
    for j in range(len(str(i))):
        temp += int(str(i)[j])
        
    if temp == a :
        lst.append(i)
    else:
        continue
        
if len(lst)==0:
    print(0)  
else:
    print(min(lst))