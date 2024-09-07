import sys

input = sys.stdin.readline



while True:
    a,b = map(int,input().split())
    try:
        if b % a ==0 :
            print('factor')

        elif a % b == 0:
            print('multiple')

        elif a== 0 and b == 0:
            break
        else:
            print('neither')

        
    except:
        break