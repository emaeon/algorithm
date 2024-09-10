import sys

input = sys.stdin.readline

n,m = map(int,input().split())

lst = list(map(int,input().split()))

start, end = 1, max(lst)

while start <= end : #벌목 높이 찾는 알고리즘
    
    mid = (start+end) // 2
    
    height = 0 #벌목된 나무 총합
    for i in lst :
        if i >= mid :
            
            height = i - mid
            
    if height >= m :
        start = mid + 1
    else :
        end = mid - 1
print(end)
            