from bisect import bisect_left, bisect_right

n = int(input())
lst = list(map(int, input().split()))
lst.sort()

m = int(input())
check = list(map(int, input().split()))

result = []
for i in check :
    left = bisect_left(lst,i)
    right = bisect_right(lst,i)

    if (right-left) > 0 :
        result.append(1)
    else:
        result.append(0)
print(*result)