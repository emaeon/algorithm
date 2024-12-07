import sys
input = sys.stdin.readline

def count(map):
    cnt = 2
    for i in map:  # 행 단위로 탐색
        one = i.count(1)
        two = i.count(2)
        three = i.count(3)

        temp = [one, two, three]  # 각 숫자의 횟수

        if 2 in temp:
            number = temp.index(2) + 1  # 2번 존재하는 값

            temp_num = 0
            for h in i: # 각 값을 꺼내서 차이 구하기
                temp_num += abs(h - number)

            if temp_num < cnt:
                cnt = temp_num
        elif 3 in temp:
            cnt = 0
            break
        else:
            pass
    return cnt

map = [list(map(int,input().split())) for _ in range(3)]
colmap = [[0]*3 for _ in range(3)]
# 행 열 뒤집기
for i in range(3):
    colmap[0][i] = map[i][0]
    colmap[1][i] = map[i][1]
    colmap[2][i] = map[i][2]


cnt1 = count(map)
cnt2 = count(colmap)

if cnt1>=cnt2 :
    print(cnt2)
else:
    print(cnt1)