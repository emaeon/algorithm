import  sys
input = sys.stdin.readline

k,n = map(int,input().split())
linelst = [int(input().rstrip()) for _ in range(k)]

def bisect(arr, t, s, e) :

    while s <= e :
        mid = (s+e)//2

        num = 0
        for i in arr :
            # if i>mid:
            num += (i//mid)
        #
        # if num == t:
        #     return e

        if num >= t:
            s = mid+1

        else:
            e = mid-1
    return e
result = bisect(linelst, n, 1, max(linelst))
print(result)