def solution(brown, yellow):
    answer = []
    a = brown+yellow
    for i in range(2,a):
        
        if a % i == 0 :
            
            if i >= a//i and ((i-2)*((a//i)-2) == yellow): #가로, 세로 길이 빼준 값이랑 yellow랑 같아야 함
                print([i, a//i])
                answer = [i,a//i]
                break
    return answer