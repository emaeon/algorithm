from itertools import permutations
import math

def is_prime(n) :
    for _ in range(2,int(math.sqrt(n))+1):
        if n % _ == 0:
            return False
    return True

def solution(numbers):
    a = list(map(str,numbers))
    answer = 0
    temp = []
    
    for i in range(1,len(a)+1):
        for j in permutations(a,i):
            word = int(''.join(j)) #튜플 합치기
            if word == 0 or word == 1:
                continue
            else :
                temp.append(word)

    temp = set(temp)
    
    for z in temp:
        if is_prime(z):
            answer += 1

    return answer