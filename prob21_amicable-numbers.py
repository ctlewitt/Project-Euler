MAX = 10000

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
num_dict = {} #num: sum of proper divisors]

#get sum of proper divisors of each number from 1 to MAX.
#get prime factors of each number; get sum of proper divisors of each number from prime factors; record sum if in bounds and != number itself
for num in range(1, MAX+1):
    prime_factors = get_prime_factors(num, primes)
    sum_proper_divisors = get_sum_proper_divisors(prime_factors, num)
    if sum_proper_divisors <= MAX and sum_proper_divisors != num:
        num_dict[num] = sum_proper_divisors

#find amicable numbers
amicable_nums = []
for num in num_dict.keys():
    sum = num_dict[num]
    if num_dict[sum] == num:
        if num not in amicable_nums:
            amicable_nums.append(num)
        if sum not in amicable_nums:
            amicable_nums.append(sum)

#add up amicable numbers
sum_amic_nums = 0
for num in amicable_nums:
    sum_amic_nums += num

#print results
print "The sum of the amicable numbers from 1 to %s is %s" %(MAX, sum_amic_nums)