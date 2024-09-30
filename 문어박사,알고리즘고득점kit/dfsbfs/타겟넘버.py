answer = 0

def dfs(numbers, target, i, value) :
    global answer
    if i == len(numbers) and value == target :
        answer +=1
        return
    elif i == len(numbers) :
        return
    
    dfs(numbers, target, i+1, value + numbers[i])
    dfs(numbers, target, i+1, value - numbers[i])

def solution(numbers, target):
    global answer
    dfs(numbers, target, 0,0)
    
    return answer