import sys

input = sys.stdin.readline

lst = [] #리스트 선언

n= int(input().rstrip()) #명령 개수

for i in range(n):
    a = input().rstrip()
    if 'push' in a: #만약 push 명령어라면
        p,num = map(str, a.split()) #명령어 숫자 분리
        lst.append(int(num)) #스택에 숫자 쌓기
    elif 'pop' in a : #만약 pop 명령어라면
        if len(lst)==0: #리스트가 비었다면
            print('-1') #-1 출력
        else: #리스트가 안비었다면
            print(lst.pop()) #스택에 맨위 꺼내면서(선입후출) 해당 숫자 출력
    elif 'size' in a: #만약 size 명령어라면
        print(len(lst)) #리스트 길이(정수 개수) 출력
    elif 'empty' in a : #만약 empty 명령어라면
        if len(lst) == 0 : #만약 스택이 비었다면
            print('1') # 1출력
        else: #안비었다면
            print('0') #0출력
    elif 'top' in a : #만약 top 명령어라면
        if len(lst)==0: #스택이 비었다면
            print(-1) #-1출력
        else: #안비었다면
            print(lst[::-1][0]) #가장 위에 있는 정수, 즉 가장 늦게들어온 정수 출력(스택은 선입후출이니 뒤집어서 맨마지막에 있는 숫자를 맨앞으로 가져와서 출력)