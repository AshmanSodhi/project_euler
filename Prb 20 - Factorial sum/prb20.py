num = 100
sum = 0
factorial = 1
for i in range(1,num+1):
    factorial = factorial*i


print(factorial)

for i in str(factorial):
    sum = sum + int(i)

print(sum)