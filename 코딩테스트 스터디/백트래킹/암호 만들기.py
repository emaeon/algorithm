import sys


def back_tracking(cnt, idx):

    # 암호를 만들었을 때
    if cnt == l:
        # 모음, 자음 체크
        vo, co = 0, 0

        for i in range(l): #암호문길이
            if answer[i] in consonant: #모음이 있으면
                vo += 1 # 모음 추가
            else:
                co += 1 # 자음 추가

        # 모음 1개 이상, 자음 2개 이상
        if vo >= 1 and co >= 2:
            print("".join(answer)) # 출력

        return

    # 반복문을 통해 암호를 만든다.
    for i in range(idx, c): # 1. range(0, 문자 길이) 2.range(1,문자길이)
        answer.append(words[i]) # 1. answer=['word[0]'], 2.answer=['word[0]','word[1]']
        back_tracking(cnt + 1, i + 1) # 1. back(1,1) #
        answer.pop() #1. answer


l, c = map(int, sys.stdin.readline().split())
words = sorted(list(map(str, sys.stdin.readline().split())))
consonant = ['a', 'e', 'i', 'o', 'u']
answer = []
back_tracking(0, 0)