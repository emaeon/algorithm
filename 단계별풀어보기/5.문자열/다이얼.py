#1을 걸려면 2초, 한칸옆에있는 숫자를 걸기 위해선 1초씩 더 걸림(+)
# 문자 입력받고 리스트로 저장
# 한 글자당 다이얼의 원소와 비교
# 원소에 존재하면 해당 원소의 인덱스 + 3이 걸리는 시간

import sys

dial=['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']

input=sys.stdin.readline

lst = list(input().rstrip())

tim=0
for j in lst :
    for i in range(len(dial)):
        if j in dial[i-1]:
            a = dial.index(dial[i-1])+3
            tim+=a
    
    
print(tim)
