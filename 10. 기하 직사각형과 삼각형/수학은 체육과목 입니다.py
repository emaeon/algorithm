import sys

input = sys.stdin.readline

lst = ['9a3','3a1','12a','a1']

new_lst=[]
for i in lst :
    for j in range(10):
        new_lst.append(i.replace('a',str(j)))
        

print(new_lst)
    