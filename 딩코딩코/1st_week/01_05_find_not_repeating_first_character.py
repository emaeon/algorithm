input = "abadabac"

def find_not_repeating_first_character(string):
    # 이 부분을 채워보세요!
    answer = []
    for alpha in string :
        if alpha not in answer :
            answer.append(alpha)
        else :
            answer.pop(answer.index(alpha))
    if answer :
        return answer[0]
    else:
        return '_'

result = find_not_repeating_first_character
print("정답 = d 현재 풀이 값 =", result("abadabac"))
print("정답 = c 현재 풀이 값 =", result("aabbcddd"))
print("정답 =_ 현재 풀이 값 =", result("aaaaaaaa"))