# if 1 -> 1(n=1) range(1,2)
# if 2 -> 2 3 4 5 6 7 (n=6) range(2, 8)
# if 3 -> 8 9 10 11 12 13 14 15 16 17 18 19 (n=12) range(8, 20)
# if 4 -> 20 ~ 37 (n=18) range(20, 38)


import sys

input=sys.stdin.readline
t=int(input().rstrip())

nums = 1 #벌집개수
cnt = 1 #카운트(칸)

while t > nums : #만약 입력한 값이 벌집 개수 보다 작은 경우에 멈춤 
    
    nums += 6 * cnt # 6의 배수만큼 한칸씩 이동
    cnt += 1 # 반복문 한번 돌때마다 카운트 증가
    
#7 -> 
print(cnt)
    