import sys

input = sys.stdin.readline

#
#문자열에서 크로아티아 알파벳 탐색
# 뽑은 문자의 다음 탐색
alpha = input().rstrip()

lst = ['c=','c-','dz=','d-','lj','nj','s=','z=']

cnt =0
for i in lst :
    if i in alpha:
        # print(alpha.count(i))
        cnt += alpha.count(i)
        alpha = alpha.replace(i, "_")
alpha=alpha.replace("_","")
cnt += len(alpha)
print(cnt)
        