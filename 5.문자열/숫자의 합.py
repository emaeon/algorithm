import sys
input=sys.stdin.readline

n=int(input().rstrip())
string=str(input().rstrip())

a=0
for i in range(n):
    a += int(string[i])
    
print(a)