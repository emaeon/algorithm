import sys


input = sys.stdin.readline

# 모든 숫자를 다 차근차근 세어보고 666들어간 경우에 카운트 하기
# 만약 카운트가 해당 숫자가 되었을 경우ㅓ멈추고 666이 들어간 해당 숫자 출력

a = int(input().rstrip())

n = 0
result =0
while True:
    
    if '666' in str(n):
        result += 1
    
    if result == a :
       print(n) 
       break
    
    n += 1
        
    
      
    