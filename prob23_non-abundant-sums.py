def is_divisible(num, divisor):
#checks if number is divisible by divisor, returns True/False accordingly
    if num % divisor == 0:
        return True
    else:
        return False


def get_prime_factors(number, primes):
#find all prime factors of number and returns a dictionary, prime_factors
    prime_factors = {}
    num = number #num is used to calculate what's left after each prime factor is divided out of the number
    next_prime = primes[0]
    next_prime_counter = 0
    while next_prime <=num:
        #check if next_prime is a prime factor of num (and therefore number)
        while is_divisible (num, next_prime):
            num = num/next_prime
            if next_prime in prime_factors.keys():
                prime_factors[next_prime] += 1
            else:
                prime_factors[next_prime] = 1
        #cue up next prime to check for factor-hood, if we're out of primes, calculate another
        next_prime_counter += 1
        if next_prime_counter >= len(primes):
            next_prime, primes = find_next_prime(next_prime, primes)
        else:
            next_prime = primes[next_prime_counter]
    return prime_factors #dict

#I might want to switch this to the faster prime finding method from problem 10.
def find_next_prime(next_prime, primes):
#finds next prime in sequence, appends it to primes, returns next_prime and list of primes
    is_prime = False
    while not is_prime:
        is_prime = True
        next_prime += 2
        for prime in primes:
            if is_divisible(next_prime, prime):
                is_prime = False
                break
    primes.append(next_prime)
    return next_prime, primes

def get_sum_proper_divisors(prime_factors, num):
#get sum of factors of number (use primes, formula for sum of factors, subtract number (b/c sum includes number as factor.)
    sum = 1
    for prime in prime_factors.keys():
        prime_power = prime_factors[prime]
        sum *= (prime**(prime_power + 1) - 1)/(prime - 1)
    sum -= num
    return sum

#initialize variables
primes = [2, 3]
num_dict = {} #num: sum of proper divisors
abundant_nums = []
abundant_sums = []

#find abundant numbers from 12 to 28123
#get prime factors of each number; get sum of proper divisors of each number from prime factors; record sum if larger than number
for num in range(12, 28123+1):
    prime_factors = get_prime_factors(num, primes)
    sum_proper_divisors = get_sum_proper_divisors(prime_factors, num)
    if sum_proper_divisors > num:
        abundant_nums.append(num)
print "abundant_nums:"
print abundant_nums

#make list of numbers that are sums of 2 abundant numbers
for count in range(0, len(abundant_nums)):
    for next_count in range(count, len(abundant_nums)):
        abundant_sums.append(abundant_nums[count] + abundant_nums[next_count])

#sort list of abundant number sums and remove duplicates
abundant_sums.sort()
abundant_sums = list(set(abundant_sums))

#find sum of all numbers from 1 to 28123 that are not in the list of abundant number sums
    #this is slightly faster because I don't have to check repeatedly if the numbers are in the abundant number sums list
counter = 0
sum = 0
for num in range(1, 28123+1):
    if num < abundant_sums[counter]:
        sum += num
    else:
        counter += 1

#print results
print sum