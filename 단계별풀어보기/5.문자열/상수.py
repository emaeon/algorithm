import sys

#두 수 입력받음 -> 두 수 뒤집기 -> 대소 비교 -> 뒤집힌 수 중 큰 값 출력

input=sys.stdin.readline

A,B=map(str,input().split())

A=A[::-1]
B=B[::-1]

if int(A) > int(B) :
    print(A)
else:
    print(B)