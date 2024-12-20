import sys
input = sys.stdin.readline
w, n = map(int,input().split())
lst = []
for _ in range(n):
    a,b = map(int,input().split())
    lst.append([a,b])

lst.sort(key = lambda x: x[1], reverse = True)

money = 0
for i in lst :
    if w == 0 :
        break

    elif w >= i[0] : #금 무게 충분하면
        w -= i[0]
        money += (i[0]*i[1])
    else: #금 무게가 수용 무게를 초과하면
        temp = i[0] - w
        i[0] -= temp
        w -= i[0]
        money += i[0]*i[1]

print(money)