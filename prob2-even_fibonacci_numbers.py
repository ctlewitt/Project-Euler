max = 4000000

total = 0

even = 2 #will cycle from 0 to 2 (0,1,2,0,1,2), if it's 2, the fib num is even
# every 3rd number will be even.  b/c of odd+even, odd+odd, (even+even never happens)

fib1 = 1
fib2 = 2
fib_next = 2

while fib_next <= max:
    #check if even, add even value, reset even counter
    if even == 2:
        total += fib_next
        even = 0
    else:
        even += 1

    #calculate next fib num and reset
    fib_next = fib1 + fib2
    fib1 = fib2
    fib2 = fib_next

print total
