import sys

input=sys.stdin.readline

#1~30번 출석번호

man = [i+1 for i in range(30)]
# print(man)
for _ in range(28):
    n=int(input().rstrip())
    man.remove(n)
    
man.sort()

print(man[0])
print(man[1])
    