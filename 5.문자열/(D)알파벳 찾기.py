
import sys

input=sys.stdin.readline

s=list('abcdefghijklmnopqrstuvwxyz') #a~z, 문자열에 list를 씌우면 한 문자씩 원소가 됨

string=list(input().rstrip())

#s에서 string안의 a의 인덱스
lst=[]
for i in s :
    if i in string :
        idx=string.index(i)
        lst.append(idx)
    else:
        lst.append(-1)
print(*lst)

##find 함수도 사용할 수 있음
# S = input()

# for x in 'abcdefghijklmnopqrstuvwxyz':
#     print(S.find(x), end = ' ')