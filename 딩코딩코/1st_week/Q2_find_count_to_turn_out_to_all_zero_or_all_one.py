import sys
input = sys.stdin.readline
string = input().rstrip()
'''
01110
popnumber = 0
1110
만약 pop number랑 pop이랑 다르면?
popnumber = 1
달라질때까지 계속 pop
pop number랑 pop이랑 달라졌다면?
cnt += 1
'''

def find_count_to_turn_out_to_all_zero_or_all_one(string):
    # 이 부분을 채워보세요!
    n = len(string)-1
    lst = list(map(int,string.rstrip()))

    one_cnt = 0
    zero_cnt = 0

    if lst[0] == 0 :
        one_cnt += 1
    else:
        zero_cnt += 1

    while n :
        temp = lst.pop(0)
        if lst[0] != temp :
            if lst[0] == 1 :
                zero_cnt += 1
            else:
                one_cnt += 1
        n -=1

    return min(one_cnt,zero_cnt)

result = find_count_to_turn_out_to_all_zero_or_all_one(string)
print(result)