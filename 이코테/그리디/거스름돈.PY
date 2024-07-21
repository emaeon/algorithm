lst = [500,100,50,10]
n = 1260

lst.sort(reverse=True)

count = 0 

for i in lst :
    count+=n//i
    n = n%i

print(count)