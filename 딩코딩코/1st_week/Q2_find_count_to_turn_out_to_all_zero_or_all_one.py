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

    answer = 0
    popnumber = lst.pop(0)
    range_inference=0
    while n :
        temp = lst.pop(0)
        if popnumber != temp :
            if len(lst) == 0:
                answer += 1
            popnumber = temp
            range_inference += 1

        if range_inference == 2:
            answer +=1
            range_inference=0
        n -=1
    return answer

result = find_count_to_turn_out_to_all_zero_or_all_one(string)
print(result)