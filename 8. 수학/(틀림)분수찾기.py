#1층
#1/1 -1
#2층
#1/2 -2, 2/1 -3 (1/n, 2/n-1) 
#3층
#3/1 -4 ,2/2 -5 ,1/3 -6 (n/1,n-1/1+1,)
#4층
#1/4 -7 ,2/3 -8 ,3/2 -9,4/1 -10
#5층
#5/1 -11 ,4/2 -12 ,3/3 -13 ,2/4 -14, 1/5 - 15
import sys
input = sys.stdin.readline
number=int(input().rstrip())

cnt = 1
rng = 1

while number > rng :
    number -= rng
    rng += 1
    cnt +=1

lst=[]
for i in range(cnt):
    if cnt % 2 == 0 :
        a = str(1 +i) +'/'+str(cnt -i)
        lst.append(a)
    else :
        a = str(cnt -i)+ '/'+str(1+i)
        lst.append(a)
        
print(lst[number-1])        