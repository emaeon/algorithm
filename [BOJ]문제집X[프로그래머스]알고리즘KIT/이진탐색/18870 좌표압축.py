from bisect import bisect_left,bisect_right

n=int(input())
lst = list(map(int,input().split()))
check = sorted(list(set((lst))))

for i in lst:
    print(bisect_left(check,i))