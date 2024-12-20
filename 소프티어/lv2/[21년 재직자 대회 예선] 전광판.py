import sys
input = sys.stdin.readline

lst = [[1,1,1,0,1,1,1],
 [0,0,1,0,0,1,0],[0,1,1,1,1,0,1],[0,1,1,1,0,1,1],
 [1,0,1,1,0,1,0],[1,1,0,1,0,1,1],[1,1,0,1,1,1,1],
 [1,1,1,0,0,1,0],[1,1,1,1,1,1,1],[1,1,1,1,0,1,1]]

t = int(input().rstrip())
for _ in range(t) :
    a,b = map(str,input().split())
    lst_a,lst_b = list(a), list(b)
    cnt = 0

    #after 숫자의 자리수가 더 많은 경우
    if len(lst_a) < len(lst_b) :
        temp = len(lst_b) - len(lst_a)
        while temp:  # 우선 바뀔숫자가 더 많다면 그만큼 b를 제거
            num = lst_b.pop(0)
            cnt += lst[int(num)].count(1)
            temp -= 1

        for i in range(len(lst_a)):

            before = lst[int(lst_a[i])]
            after = lst[int(lst_b[i])]

            for j in range(7):
                if before[j] != after[j]:
                    cnt += 1
                else:
                    pass
        print(cnt)
    # before 숫자의 자리수가 더 많은 경우
    elif len(lst_a) > len(lst_b):
        temp = len(lst_a) - len(lst_b)

        while temp:  # 우선 바뀔숫자가 더 많다면 그만큼 a를 제거
            num = lst_a.pop(0)
            cnt += lst[int(num)].count(1)
            temp -= 1

        for i in range(len(lst_a)):

            before = lst[int(lst_a[i])]
            after = lst[int(lst_b[i])]

            for j in range(7):
                if before[j] != after[j]:
                    cnt += 1
                else:
                    pass
        print(cnt)
    # 숫자 자리수가 동일한 경우
    else:

        for i in range(len(lst_a)):

            before = lst[int(lst_a[i])]
            after = lst[int(lst_b[i])]

            for j in range(7):
                if before[j] != after[j]:
                    cnt += 1
                else:
                    pass
        print(cnt)