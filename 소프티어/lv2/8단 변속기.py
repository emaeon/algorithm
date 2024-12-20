import sys
input = sys.stdin.readline

gear = list(map(int,input().split()))

first = gear[0]
asc_cnt = 0
desc_cnt = 0

for i in range(1,len(gear)):
    if (gear[i]-first) == 1:
        first = gear[i]
        asc_cnt +=1
    elif (gear[i]-first) == -1:
        first = gear[i]
        desc_cnt += 1
    else:
        break

if asc_cnt == 7 :
    print('ascending')
elif desc_cnt == 7 :
    print('descending')
else :
    print('mixed')
