n = int(input())
ans = -1
# 최소 개수 > 5키로 봉투 최대한 사용, 3키로만 사용할 수도 있는 점을 통해 5를 0개 쓰는 경우 까지 루프 돌리기
# n//5 ~ 0 까지 루프
for cnt_5 in range(n//5,-1,-1) :
    cnt_3 = (n - (cnt_5*5)) // 3 #5키로 봉투랑 뺀 무게를 3키로 봉지 수로 계산

    if cnt_5*5 + cnt_3*3 == n : # 정답 찾음
        ans = cnt_5 + cnt_3
        break
print(ans)