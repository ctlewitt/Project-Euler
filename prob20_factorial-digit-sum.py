def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


factorial_100 = factorial(100)

sum = 0
for digit in str(factorial_100):
    sum += int(digit)

print "sum: " + str(sum)