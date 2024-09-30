from itertools import permutations, combinations

def solution(k, dungeons):
    answer = -1
    for item in permutations(dungeons,len(dungeons)):
        temp = 0
        temp_k = k
        for i in item :
            if temp_k >= i[0] :
                temp_k -= i[1]
                temp += 1
            else :
                break
        if temp > answer :
            answer = temp
    
    return answer