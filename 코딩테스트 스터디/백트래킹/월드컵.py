import sys
from itertools import combinations

input = sys.stdin.readline
def back(round): #총 라운드를 받음
    global ans
    if round == 15 : #마지막 라운드
        ans = 1
        for i in res :
            if i.count(0) != 3:
                ans = 0
                break
                #마지막 라운드까지 마쳤을 떄 모든 카운트 0이어야 함
        return
    
    t1, t2 = game[round]
    for x,y in ((0,2),(1,1),(2,0)):
        if res[t1][x] >0 and res[t2][y] >0: #승 무 패의 값이 남아 있다면
            #승패, 무무, 패승이 가능할 때 마킹
            res[t1][x] -= 1 #
            res[t2][y] -= 1
            back(round +1)
            #두 국가 간 경기에서 3가지 케이스가 모두 일어날 수 있기 때문에 복구해준다
            res[t1][x] += 1
            res[t2][y] += 1
            
lst=[]
game = list(combinations(range(6),2)) # 6개 국가별 경기 조합
for _ in range(4):
    a = list(map(int,input().split()))
    res =[a[i:i+3] for i in range(0,16,3)] # 팀별 승패무 기록
    ans = 0 #결과 담을 변수 초기화
    back(0)
    lst.append(ans)
    
    

print(*lst)
            
    

