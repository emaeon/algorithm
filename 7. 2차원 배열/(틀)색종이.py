arr = [[0]*100 for _ in range(100)]
arr

import sys

input=sys.stdin.readline

t= int(input().rstrip())

for _ in range(t):
    x, y = map(int, input().split())
    
    for i in range(x,x+10):
        for j in range(y,y+10):
            arr[i][j] = 1           

result=0
for i in arr:
    result+= i.count(1)

print(result)

# import sys

# input=sys.stdin.readline

# t= int(input().rstrip())

# lst_x=[]
# lst_y=[]
# for _ in range(t):
#     x, y = map(int, input().split())
    
#     lst_x.append([i for i in range(x,x+11)])
#     lst_y.append([j for j in range(y,y+11)])


# tempx=[]
# tempy=[]
# for i in lst_x:
#     tempx += i
# for j in lst_y:
#     tempy += j

# answer_x=[]
# answer_y=[]
# for i in tempx:
#     if tempx.count(i)>=2:
#         answer_x.append(i)

# for j in tempy:
#     if tempy.count(j)==t:
#         answer_y.append(j)
# print(set(answer_x))
# print(set(answer_y))

# print(300-(len(set(answer_x))*len(set(answer_y))))


