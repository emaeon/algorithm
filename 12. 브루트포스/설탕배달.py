import sys

input = sys.stdin.readline

n = int(input().rstrip())

cnt = 0

while True :
    if n%5 != 0:
        n -= 5
        cnt += 1

        if n % 5 == 0 :
            cnt += n//5
            print(cnt)
            break
        elif n % 3 == 0 :
            cnt += n//3
            print(cnt)
            break
        
        
        
    if 3< n < 5 or n<3:
        print(-1)
        break
                
    



# result = 0

# if (n-5) % 5 == 0 :
#     result += n//5
# elif (n-5) % 3 == 0 :
#     result+=((n-5)//3) +1
# elif n%5 == 3:
#     result += (n//5) +1
# elif n %3 == 0 :
#     result += n//3

# if result == 0 :
#     print(-1)
# else:
#     print(result)