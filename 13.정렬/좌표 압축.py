import sys

input = sys.stdin.readline

n=int(input().rstrip())
lst = list(map(int, input().split()))

lst2=sorted(list(set(lst)))

for i in range(len(lst)):
    if lst[i] in lst2:
        print(len(lst2[:i]), end=" ")
    

# for i in lst:
#     print(lst2, end=" ")

