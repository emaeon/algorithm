from bisect import bisect_left, bisect_right
import sys

input = sys.stdin.readline
n, x= map(int, input().split())
lst = list(map(int,input().split()))

result = bisect_right(lst,x)-bisect_left(lst,x)

if result == 0 :
    print(-1)
else :
    print(result)
