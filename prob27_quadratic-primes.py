from math import sqrt

MAX_PRIME = 1997001
FIRST_PRIME = 2
MAX_CHECK = sqrt(MAX_PRIME)

#functions to generate list of primes

def mark_multiples(next_prime, num_dict):
    num_dict[next_prime] = "prime"
    for multiple in range(next_prime ** 2, MAX_PRIME, next_prime * 2): #skip every other multiple to avoid evens
        num_dict[multiple] = "not prime"
    return num_dict

def find_next_prime(next_prime, num_dict):
    for num in num_dict.keys():#WAS  range(next_prime + 1, MAX_CHECK):
        if num > next_prime:
            if num_dict[num] == "":
                next_prime = num
                break
    return next_prime

def set_up_num_dict():
#set up num_dict of numbers to be marked "prime" or "not prime"
#default is "" when not yet checked
    num_dict = {}
    for number in range(3, MAX_PRIME, 2):
        num_dict[number] = ""
    return num_dict

def generate_primes():
    #initialize variables and values
    num_dict = set_up_num_dict()
    #start with FIRST_PRIME (2) already established
    num_dict[FIRST_PRIME] = "prime"
    primes = [FIRST_PRIME]
    next_prime = FIRST_PRIME

    while next_prime < MAX_CHECK:
        next_prime = find_next_prime(next_prime, num_dict)
        num_dict = mark_multiples(next_prime, num_dict)

    for num in num_dict.keys():
        if num_dict[num] == "prime" or num_dict[num] == "":
            primes.append(num)
    primes.sort()
    return primes

def calculate_possible_primes(a, b, primes):
#    print "a: " + str(a) + " b: " + str(b)
    #for a given a, b combination, generates list of possible primes and checks if they are primes
    #calc_primes = []
    primes_index = 0
    n = 0
    all_primes = True
    while all_primes:
        possible_prime = n**2 + a*n + b
        if possible_prime not in primes:
            all_primes = False
#PUT THIS BACK LATER
#        all_primes, primes_index = is_prime(possible_prime, primes, primes_index)
        n += 1
#        print possible_prime,
#    print
    return n #equal to number of successful primes

def is_prime(possible_prime, primes, primes_index):
    #checks if a given number is prime by comparing it with the list of primes
    is_prime = False
    while possible_prime > primes[primes_index]:
        primes_index += 1
    if possible_prime == primes[primes_index]:
        is_prime = True
    #else: is_prime remains False
    return is_prime, primes_index



#generate list of primes below 1997001 (this is a=999, b=999, n=999, largest possible number considered.)
primes = generate_primes()
max_primes = 0
max_a = 0
max_b = 0

#go through each a, b combination (use double for loop)
for a in range(-999, 1000):
    for b in range(-999, 1000):
    #generate list of possible primes, count how many are really primes
        num_primes = calculate_possible_primes(a, b, primes)
        #compare num_primes with max_primes and set new max values if num_primes is the new winner
        if num_primes > max_primes:
            max_primes = num_primes
            max_a = a
            max_b = b
#            print "a " + str(max_a)
#            print "b " + str(max_b)
#            print "num_primes " + str(num_primes)

#when done with all numbers, print out product of max_a and max_b
print max_a
print max_b
print max_a * max_b