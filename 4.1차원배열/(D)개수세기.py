import sys

input = sys.stdin.readline

n=int(input().rstrip())
lst = list(map(int,input().split())) #list로 받을 수 있음을 유의
    
v=int(input().rstrip())

print(lst.count(v))