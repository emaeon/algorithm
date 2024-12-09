def find_max_occurred_alphabet(string):
    # 이 부분을 채워보세요!

    #ord는 문자 -> 아스키코드
    #chr은 아스키코드 -> 문자

    array = [0]*(ord('z')-ord('a'))

    for word in string:
        if word.isalpha() : #문자열인지 확인하는 방법
            array[ord(word)-ord('a')] += 1

    return chr(array.index(max(array))+ord('a'))


result = find_max_occurred_alphabet
print("정답 = i 현재 풀이 값 =", result("hello my name is dingcodingco"))
print("정답 = e 현재 풀이 값 =", result("we love algorithm"))
print("정답 = b 현재 풀이 값 =", result("best of best youtube"))