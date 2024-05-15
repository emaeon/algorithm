import sys

input = sys.stdin.readline

a,b = map(int,input().split())

while True:
    try:
        if (b/a).is_integer() :
            print('factor')
            break
        elif (a/b).is_integer() :
            print('multiple')
            break
        elif a== 0 and b == 0:
            break
        else:
            print('neither')
            break
        
    except:
        break