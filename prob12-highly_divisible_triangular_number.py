#THOUGHTS:
#Factors come in pairs.  The factor in a factor-pair of a number is below the sqrt of the number; the second is above it.
#All factors-pairs of a number are split/centered around its sqrt like this.  So, for a number to have at least 500 factors,
#it must have 250 factor pairs.  250 factors are below the sqrt and 250 are above it.
#Therefore, since there is no point in calculating the number of factors for numbers who obviously have less than 500 factors,
#we should begin calculating the number of factors for numbers whose sqrt is greater than 250, so there are at least 250
#numbers (that could possibly be factors) below the sqrt.  Therefore, we should only start calculating the number of factors
#in each triangle for triangles with values above 250^2, or 62500.

#We do not need to calculate the exact factors to find the number of factors.  We only need to calculate the prime factorization
#(or rather the multiplicity of each prime in the prime factorization, really) in order to calculate the number of factors
#the number would have.  For a number N, whose prime factorization is (p1^n1)*(p2^n2)*(p2^n3)...(pm^nm), the number of
#factors N has is equal to (1+n1)(1+n2)(1+n3)...(1+nm).  (Add one to the multiplicity of each of the prime factors and
#then multiply them by each other.)
# (Mathematical formula for finding num factors from prime factorization was given by user lurflurf on this website: http://www.physicsforums.com/showthread.php?t=80936)
#As a side note, the factors of a number could probably be calculated from its prime factors using recursion, but that's outside the scope
#of this question.

MIN_FACTORS = 500

def get_next_triangle(counter, triangle):
    next_triangle = triangle + counter
    return next_triangle

def is_divisible(num, divisor):
#checks if number is divisible by divisor, returns True/False accordingly
    if num % divisor == 0:
        return True
    else:
        return False

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

def find_prime_factors(triangle, primes):
#find all prime factors of triangle
    prime_factors = {}
    num = triangle #num is used to calculate what's left after each prime factor is divided out of the triangle
    next_prime = primes[0]
    next_prime_counter = 0
    while next_prime <=num:
        #check if next_prime is a prime factor of num (and therefore triangle)
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
    return prime_factors


def find_num_factors(triangle, primes):
#find the number of factors triangle has, based on its prime factorization
    prime_factors = find_prime_factors(triangle, primes)
    #calculate number of factors based on prime factorization
    num_factors = 1
    for prime_factor in prime_factors.keys():
        num_factors *= 1 + prime_factors[prime_factor]
    return num_factors

#initialize variables
counter = 0
triangle = 0
primes = [2, 3]

#get first set of triangles, don't calculate factors because they can't have more than MIN_FACTORS factors (see earlier explanation)
while triangle < (MIN_FACTORS/2)**2:
    counter += 1
    triangle = get_next_triangle(counter, triangle)

#continue finding triangles, start calculating factors
still_looking = True
while still_looking:
    counter += 1
    triangle = get_next_triangle(counter, triangle)
    num_factors = find_num_factors(triangle, primes)
    if num_factors >= 500:
        still_looking = False
print "The first triangle with over 500 factors is " + str(triangle) + "."
print "It has " + str(num_factors) + " factors."