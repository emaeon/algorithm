input = 20

def is_prime(number):
    for i in range(2,number+1):
        if number%i==0 :
            if i == 1 :
                pass
            elif i == number:
                pass
            else:
                return False
    return number

def find_prime_list_under_number(number):
    answer = []
    for n in range(2,number+1):
        temp = is_prime(n)
        if temp != False:
            answer.append(temp)
        else:
            pass
    return answer

result = find_prime_list_under_number(input)
print(result)