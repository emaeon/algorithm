import sys

input=sys.stdin.readline
#각 차원 별 인덱스 0 저장 -> 인덱스 1 저장 -> 인덱스 3 저장 ...
#만약 out of index면? 무시하고 그다음으로 
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
