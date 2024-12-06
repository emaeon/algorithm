import sys
input = sys.stdin.readline

n = int(input())
home = list(map(int,input().split()))

result = 0 #결과
for i in range(2,max(home)+1) : #연탄 반지름을 위해 제일작은 제약조건 2부터 제일큰값까지 하나씩 대입해보기
    temp_cnt = 0 #나눌 수 있는 최대값
    for j in home :
        if j%i == 0 : #임시 연탄의 반지름이 난로의 배수면
            temp_cnt +=1
        else:
            pass

    if result < temp_cnt :
        result = temp_cnt

print(result)