sum = 0
sumqs = 0

for i in range(1,101):
    sum = sum + i

for i in range(1,101):
    squ = i*i
    sumqs = sumqs + squ

sumsq = sum*sum
print(sumsq)
print(sumqs)

print(sumsq - sumqs)