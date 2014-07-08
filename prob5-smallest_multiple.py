#Initial ideas:
#Keep a prime factor dictionary for the lowest common multiple
#Use dictionaries to keep track of the prime factors for each number
#Every additional prime factor that isn't already in the LCM dictionary needs to be added to it


#from prob3-largest_prime_factor import find_next_prime, is_divisible
from math import sqrt

MAX_NUM = 20

#if import statement had worked, would not need to paste this def here
def is_divisible(num, divisor):
    if num % divisor == 0:
        return True
    else:
        return False

#if import statement had worked, would not need to paste this def here
def find_next_prime(next_prime, max_check):
#finds next largest prime after next_prime, if lower than max_check, adds it to the list of primes, and returns its value
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

def find_primes(primes):
#must start with primes = [2,3]
#returns list of primes up to MAX_NUM
    next_prime = primes[len(primes)-1]
    while next_prime < MAX_NUM:
        next_prime = find_next_prime(next_prime, MAX_NUM)
        #finds next prime and appends it to primes, if it is less than MAX_NUM
    return primes

def find_prime_factors(num):
#returns dictionary of prime factors of num
    num_factors = {}
    for prime in primes:
        while is_divisible(num, prime):
            if prime in num_factors.keys():
                num_factors[prime] += 1
            else:
                num_factors[prime] = 1
            num = num / prime
    return num_factors
  
def update_lcm_factors(lcm_factors, num_factors):
#returns updated lcm_factors with any additional factors from num_factors
    for prime_factor in num_factors.keys():
        if prime_factor not in lcm_factors.keys(): #prime_factor NOT IN lcm_factors.keys()
            lcm_factors[prime_factor] = num_factors[prime_factor]
        elif num_factors[prime_factor] > lcm_factors[prime_factor]: #prime_factor IN lcm_factors.keys()
            lcm_factors[prime_factor] = num_factors[prime_factor]
    return lcm_factors

def find_product(lcm_factors):
#returns the product of all the prime factors contained in dictionary
    product = 1
    for prime_factor in lcm_factors.keys():
        product *= prime_factor ** lcm_factors[prime_factor]
    return product

lcm_factors = {}
primes = [2, 3]
primes = find_primes(primes)
for num in range(1, MAX_NUM + 1):
    num_factors = find_prime_factors(num)
    lcm_factors = update_lcm_factors(lcm_factors, num_factors)

lcm = find_product(lcm_factors)
print lcm
