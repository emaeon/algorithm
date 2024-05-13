# if 1 -> 1(n=1) range(1,2)
# if 2 -> 2 3 4 5 6 7 (n=6) range(2, 8)
# if 3 -> 8 9 10 11 12 13 14 15 16 17 18 19 (n=12) range(8, 20)
# if 4 -> 20 ~ 37 (n=18) range(20, 38)


import sys

input=sys.stdin.readline
t=int(input().rstrip())
cnt = 1
nums = 1

while t > nums :
    nums += 6 * cnt
    cnt += 1
print(cnt)
    