import sys

input = sys.stdin.readline

# print(sum([1,2,3,4]))
while True:
    
    num = int(input().rstrip())
    if num <0 :
        break
    temp_lst=[]
    for i in range(1,num):
        if num % i == 0 :
            temp_lst.append(i)
    temp_lst.sort()        
    if sum(temp_lst) == num :

        print(num,'=',end=" ")
        print(*temp_lst, sep=" + ")
    else:
        print(num,'is NOT perfect.')
    