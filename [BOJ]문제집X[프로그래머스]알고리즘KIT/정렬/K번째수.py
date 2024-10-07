def solution(array, commands):
    answer = []
    
    for lst in commands :
        i,j,k = lst[0], lst[1], lst[2]
        narr = sorted(array[(i-1):j])
        answer.append(narr[k-1])
        
    return answer