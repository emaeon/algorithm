import sys

input = sys.stdin.readline
n = int(input().rstrip())

for _ in range(n):
    a = list(input().rstrip())

    if a[0] ==")":
        print("NO")
    
    elif a[::-1]=="(":
        print("NO")
    
    elif a.count("(") != a.count(')'):
        print("NO")
        
    elif a[0]=="(":
        
        cnt1, cnt2 = 0, 0
        for i in a :
            if i == '(':
                cnt1 += 1
            if i == ')' :
                cnt2 += 1
            if cnt2 > cnt1 :
                print('NO')
                break
        
        if cnt1 == cnt2:
            print('YES')