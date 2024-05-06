import sys

input = sys.stdin.readline

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
        