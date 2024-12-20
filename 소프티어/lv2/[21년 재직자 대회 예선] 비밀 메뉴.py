import sys
from collections import deque

input = sys.stdin.readline

m,n,k = map(int, input().split())
scrt_lst = list(map(int, input().split()))
bttn_lst = list(map(int, input().split()))

result = 'normal'

while bttn_lst :
    if len(bttn_lst) < len(scrt_lst):
        break

    if bttn_lst[0] != scrt_lst[0] :
        bttn_lst.pop(0)

    else:

        result = 'secret'
        ran = 0
        for i in range(len(scrt_lst)):
            if scrt_lst[i] != bttn_lst[i] :
                result = 'normal'
                break

        if result == 'secret':
            break
        else :
            bttn_lst.pop(0)
            '''
            반례 조심
            m : 3313
            k : 33313 일 경우
            m - 331 , k = 333 에서 어긋나서 
            k -> 313부터 시작하게 되면 normal이 결과로나옴
            이게아닌, 앞에 3만 제외하고 다시 하는게 맞음
            '''


print(result)