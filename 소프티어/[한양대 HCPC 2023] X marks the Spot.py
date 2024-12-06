import sys

input = sys.stdin.readline
n = int(input().rstrip())

result = []
cnt = 0

while True:
    if cnt == n:
        break

    s, t = map(str, input().split())
    idx = s.upper().index('X')

    temp = t[idx].upper()  # 대문자로 변경
    result.append(temp)
    cnt += 1

print(*result, sep='')