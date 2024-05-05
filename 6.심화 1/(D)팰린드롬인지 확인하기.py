import sys

input=sys.stdin.readline

#팰린드롬 앞으로 읽을 때와 거꾸로 읽을 떄 똑같은 단어

string = input().rstrip()

#단어 길이 만큼 반복, 첫단어와 마지막단어/두번쨰와 마지막-1단어 같은지 확인
lst=[]
for i in range(len(string)):
    if string[i] == string[len(string)-1-i]:
        lst.append('yes')
    else:
        lst.append('no')

if lst.count('no') == 0 :
    print(1)
else:
    print(0)