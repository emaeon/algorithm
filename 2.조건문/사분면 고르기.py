import sys
input=sys.stdin.readline
a = int(input())
b = int(input())

#1 -> + +
#2 -> - +
#3 -> - -
#4 -> + -
if a>0 and b>0 :
    print('1')
elif a<0 and b>0 :
    print('2')
elif a<0 and b<0 :
    print('3')
elif a>0 and b<0 :
    print('4')