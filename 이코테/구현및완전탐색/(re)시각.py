import sys

input = sys.stdin.readline

n=int(input().rstrip())

cnt = 0

for i in range(n+1):
    for j in range(60):
        for z in range(60):
            #매 시각 안에 '3'이 포함되어 있다면 카운트 증가
                if '3' in str(i)+str(j)+str(z):
                    cnt +=1

print(cnt)

    
    