from math import sqrt

num = 600851475143
largest_prime_factor = num
max_check = int(sqrt(num))

next_prime = 2
primes = [next_prime]

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
        if next_prime > max_check:
            return next_prime
        for prime in primes:
            if is_divisible(next_prime, prime):
                is_prime = False
                break
    primes.append(next_prime)
    return next_prime

#check 2, then make next_prime = 3 for more efficient looping
if is_divisible(num, next_prime):
    num = num/next_prime
    largest_prime_factor = next_prime
next_prime=3
primes.append(next_prime)

while next_prime < max_check and next_prime <= num:
    if is_divisible (num, next_prime):
        num = num/next_prime
        largest_prime_factor = next_prime

    next_prime = find_next_prime(next_prime)

print largest_prime_factor
