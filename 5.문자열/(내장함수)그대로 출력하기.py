import sys

input=sys.stdin.readline

for _ in range(100):
    
    try:
        print(input().rstrip())
        
    except:
        break
    
# while True:
#     try:
#         print(input())
#     except EOFError: #End Of File Error 입력값이 없는 경우
#         break