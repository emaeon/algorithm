from itertools import permutations
def solution(numbers):
    lst = []
    for i in numbers :
        lst.append(str(i))
        
    lst.sort(key = lambda x : str(x)*3, reverse=True)
    return str(int(''.join(lst)))
    
    
    
    # max = 0
    # for num in permutations(numbers,len(numbers)):
    #     t = ''.join(list(map(str,num)))
    #     word = int(t)
    #     if max < word:
    #         max = word
    # return str(max)