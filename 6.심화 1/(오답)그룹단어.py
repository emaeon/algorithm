import sys

# input=sys.stdin.readline



# #문자열 길이만큼 문자의 각 글자 추출
# # 만약 특정 글자의 개수가 2개 이상이라면?
# # 0번째 문자가 2번 이상 나온다 -> 0:2 인덱스 문자 추출
# # 추출된 문자열의 특정 글자 count가 전체 문자열 개수 와 동일하다 -> cnt+1 아닐경우 pass

# t = int(input().rstrip())

# cnt=0
# for _ in range(t):
#     word=input().rstrip() 
    
#     if len(set(list(word))) == len(word):
#         cnt+=1
#         continue #해당 단어는 바로 반복문 빠져나와야함  
#     else:
#         for i in range(len(word)):
#             idx=word.count(word[i])
#             if idx >= 2 :
#                 sub_word=word[i:i+idx]
#                 temp=word[i:]
#                 if temp.count(word[i]) == idx :
#                     temp=temp.replace(word[i],"")                    
#                 else :
#                     print('탈락'+word)
#                     break 
        

# print(cnt)


t = int(input().rstrip())

n = t
for _ in range(t):
    
    word = input().rstrip()
    
    for i in range(len(word)-1):
        if word[i] == word[i+1]:
            pass
        elif word[i] in word[i+1:]:
            n -=1
            break
print(n)