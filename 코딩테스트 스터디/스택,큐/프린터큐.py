t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    data = list(map(int, input().split()))
    
    result = 1
    while data:
        if data[0] < max(data):
            data.append(data.pop(0))

        else:
            if m == 0: break

            data.pop(0)
            result += 1

        m = m - 1 if m > 0 else len(data) - 1

    print(result)

# import sys
# from collections import deque
# import itertools

# queue=deque()
# input = sys.stdin.readline

# case = int(input().rstrip())

# for _ in range(case):
    
#     n,idx = map(int, input().split())
#     weight = deque(map(int, input().split()))
    
#     temp={}
#     cnt=0
#     for i,z in list(weight):
#         print(list(itertools.islice(weight,1,len(weight))))
#         if weight[0] >= max(weight):
#             weight.popleft()
#             cnt+=1
#             temp[i] = cnt
#         else:
#             weight.append(weight.popleft())
#     print(temp)