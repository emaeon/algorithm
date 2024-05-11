import sys

input=sys.stdin.readline

# 0: 2(3-1)*2 , 1: 3(4-1)*3 , 2: 5(6-1)*5, 3: 9(10-1)*9, ...
#3,4,6,10(1~2~4~8~)
#0 : 4 = 2**(1) * 2**(1),
#1 : 9 = 2**(1)=1*2**(1)+1,
# 2**3 25 = 2**2,
# 2**4

t= int(input().rstrip())
degree = (2**(t)+1)
print(degree*degree)