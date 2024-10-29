import sys
input = sys.stdin.readline

n,m = map(int,input().split())
lst = list(map(int,input().split()))
# cut = list(range(1,max(lst)))

def bisect(tree, target, s, e):
    maxh = 0
    while s <= e :
        mid = (s+e)//2

        h=0
        for i in tree :
            if i > mid:
                h += (i - mid)

        if h == target:
            return mid

        elif h > target:
            s = mid + 1
            maxh = mid #이거 해줘야 함
        else:
            e = mid - 1

    return maxh

result = bisect(lst, m,0,max(lst)) #0에서 시작 해줘야 함

print(result)