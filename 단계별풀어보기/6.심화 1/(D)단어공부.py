import sys

input=sys.stdin.readline

string=list(input().rstrip().lower())
str_set=list(set(string))
#str_set에서 하나씩 꺼내면서 string에서 count (개수 세기)
# cnt에 개수 하나씩 저장
# cnt가 중복이면 ?출력
# cnt 중복이 아닐 때
# str_set의 단어 중 가장 카운트 많이 된 인덱스 확인
# 인덱스에 해당하는 값 출력

cnt=[]
for i in str_set:
    cnt.append(string.count(i))

if cnt.count(max(cnt)) > 1 :
    print('?')
else :
    idx = cnt.index(max(cnt))
    print(str_set[idx].upper())



