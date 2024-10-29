import sys
input= sys.stdin.readline

def bisect(arr, cut,target, start, end) :
    while start <= end:
        mid = (start+end)//2

        a = 0
        for i in arr :
            if i > cut[mid]:
                a += (i - cut[mid])

        if a == target :
            return temp[mid]

        elif a > target : # a가 크면 mid가 작은것
            start = mid + 1

        else:
            end = mid - 1
    return None

n, m = map(int,input().split())

lst = list(map(int, input().split()))

temp = list(range(min(lst), max(lst)+1))

a = bisect(lst,temp, m,0,len(temp)-1)
print(a)