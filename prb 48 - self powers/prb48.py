sum = 0
for i in range(1,1001):
    d = i**i
    sum = sum + d
str1 = str(sum)

lastTen = str1[-10:]
print(lastTen)