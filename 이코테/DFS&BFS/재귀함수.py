def recursive(i):
    if i == 100 :
        return
    print(i,'번',i+1,'재귀 함수 호출합니다.')
    
    recursive(i+1)
    print(i, '종료합니다')

recursive(1)