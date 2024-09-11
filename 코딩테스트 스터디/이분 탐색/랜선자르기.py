import sys

input = sys.stdin.readline

#1 input 받기
k, n = map(int, input().split())
lst = [int(input().rstrip()) for i in range(k)]
#2. start,end 설정
start, end = 1, max(lst) #처음과 끝 위치

#3. 반복문 만들기
while start<=end : #적절한 랜선의 길이 찾는 알고리즘 
    #mid 만들기
    mid = (start+end)//2 #중간 위치
    
    #숫자 세기 시작
    lines = 0 #랜선 수
    for i in lst : #선 하나씩 꺼내기
        lines += i // mid #분할 된 랜선 수
        
    if lines >= n : #랜선의 개수가 분기점
        start = mid + 1
        
    else :
        end = mid -1 

print(end)