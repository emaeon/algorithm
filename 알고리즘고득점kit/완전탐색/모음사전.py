from itertools import permutations, product

def solution(word):
    answer = 0
    lst = []
    for i in range(1,6):
        for j in product(['A','E','I','O','U'],repeat=i):
            lst.append(''.join(j))
                
    lst.sort()
    answer = lst.index(word)+1

    return answer