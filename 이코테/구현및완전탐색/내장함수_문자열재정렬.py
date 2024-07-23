import sys
input=sys.stdin.readline


n = (input())

num = 0
new_string=''
for i in n:
    if ord(i) in range(ord('1'),ord('9')):
        num+=int(i)
    else:
        new_string+=i
        
        
sort_n=sorted(new_string)

string=''
for j in sort_n:
    string+=j
    
print(string+str(num))
        

    
