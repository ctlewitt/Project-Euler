MAX_LENGTH = 1000
fib1 = 1
fib2 = 1
fib_next = fib2
fib_count = 2

while len(str(fib_next)) < MAX_LENGTH:
    #calculate next fib num, count fibs, and reset
    fib_next = fib1 + fib2
    fib_count += 1
    fib1 = fib2
    fib2 = fib_next

print "The index of the first Fibonacci number with over 1000 digits is " + str(fib_count) + "."
