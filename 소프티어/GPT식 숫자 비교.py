import sys
input = sys.stdin.readline

n = int(input().rstrip()) # 몇 개 받을지
numlst = [input().rstrip() for _ in range(n)]

def gpt(value):
    if '.' in value:
        x,y = value.split('.')
        return(int(x), int(y))
    else:
        return(int(value),-1)



print(*sorted(numlst,key= lambda x :gpt(x)),sep='\n')