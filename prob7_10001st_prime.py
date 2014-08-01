MAX_COUNT = 10001

def find_next_prime(next_prime):
#finds next largest prime after next_prime and returns its value
    is_prime = False
    while not is_prime:
        is_prime = True
        next_prime += 2
        for prime in primes:
            if is_divisible(next_prime, prime):
                is_prime = False
                break
    return next_prime

def is_divisible(num, divisor):
#checks if num is divisible by divisor and returns True/False accordingly
    if num % divisor == 0:
        return True
    else:
        return False

def find_primes(primes, num_primes):
#returns list of primes of length MAX_COUNT
#(must start with primes = [2,3] and num_primes = 2)
    next_prime = primes[len(primes)-1]
    while num_primes < MAX_COUNT:
        next_prime = find_next_prime(next_prime)
        primes.append(next_prime)
        num_primes += 1
    return primes

primes = [2, 3]
num_primes = 2
primes = find_primes(primes, num_primes)
print primes[len(primes)-1]