import sys

input=sys.stdin.readline
#각 차원 별 인덱스 0 저장 -> 인덱스 1 저장 -> 인덱스 3 저장 ...

lst=[]
wordlen=0
for _ in range(5):
    word = input().rstrip()
    lst.append(word)
    if len(word) > wordlen:
        wordlen=len(word)

string=''
for i in range(wordlen):
    for j in lst:
        try:
            string+=j[i]
        except:
            continue
        
        
print(string)
    
