import sys

input=sys.stdin.readline
#높이 : v, 올라가는 높이 : A, 자는 동안 미끄러진 높이 : B
# 정상에서는 미끄러지지 않음
# 시간 생각해야 함
# Aa - Ba +B = v

A, B ,V = map(int, input().split())
a = (V -B)/ (A-B)
if a == int(a):
    print(int(a))
else:
    print(int(a)+1)


#오답 1
# A, B ,V = map(int, input().split())


# for a in range(V+1):
#     if (A*a)-(B*(a-1)) >= V:
#         print(a)
#         break
#     else:
#         pass
    
# 오답 2
# a = V
# while True :

#     if (A*a)-(B*(a-1)) < V:
#         print(a+1)
#         break
#     else:
#         a -= 1