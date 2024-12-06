from bisect import bisect_left, bisect_right

n=int(input())
lst = list(map(int,input().split()))
lst.sort()
m=int(input())
check = list(map(int,input().split()))
result=[]
for i in check :
    right = bisect_right(lst,i)
    left = bisect_left(lst, i)

    num = right - left
    result.append(num)

print(*result)