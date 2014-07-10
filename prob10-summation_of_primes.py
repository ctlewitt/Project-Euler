from math import sqrt

MAX_CHECK = 2000000

def is_divisible(num, divisor):
    if num % divisor == 0:
        return True
    else:
        return False

def find_next_prime(next_prime):
    is_prime = False
    while not is_prime:
        is_prime = True
        next_prime += 2
        if next_prime > MAX_CHECK:
            return next_prime
        for prime in primes:
            if is_divisible(next_prime, prime):
                is_prime = False
                break
    primes.append(next_prime)
    print next_prime
    return next_prime


next_prime = 3
primes = [2, 3]
sum = 0

while next_prime < MAX_CHECK:
    next_prime = find_next_prime(next_prime)

for prime in primes:
    sum += prime

print "sum of primes below " + str(MAX_CHECK) + " is " + str(sum) + "."