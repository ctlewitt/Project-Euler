#Uses the Sieve of Eratosthenes
#I am using the following optimizations:
#1) Don't mark off any multiples of 2; don't include them in data structures, etc
#2) Only check every other multiple of each prime (to avoid the evens, see #1)
#3) Start checking at the square of each prime, since the smaller multiples were already checked by smaller primes
#(since this still involves calculating the square, I only save some computer-brain-effort
#4) Stop evaulating if numbers are prime when I get to the sqrt of the max prime value I want to find
#(remember how I start marking off multiples at the square of each prime? no point in going higher)
#This eliminates the need to do anything once I reach ~1415.  That's huge, when we're talking about 2x10^6

from math import sqrt
from timeit import timeit

MAX_NUM= 2000000
FIRST_PRIME = 2
MAX_CHECK = sqrt(MAX_NUM)


def mark_multiples(next_prime, num_dict, max_num):
    num_dict[next_prime] = "prime"
    for multiple in range(next_prime ** 2, max_num, next_prime * 2): #skip every other multiple to avoid evens
        num_dict[multiple] = "not prime"
    return num_dict

def find_next_prime(next_prime, num_dict):
    for num in num_dict.keys():#WAS  range(next_prime + 1, MAX_CHECK):
        if num > next_prime:
            if num_dict[num] == "":
                next_prime = num
                break
    return next_prime


def set_up_num_dict(max_num):
#set up num_dict of numbers to be marked "prime" or "not prime"
#default is "" when not yet checked
    num_dict = {}
    for number in range(3, max_num, 2):
        num_dict[number] = ""
    return num_dict

def get_primes(max_num):
    #initialize variables and values
    num_dict = set_up_num_dict(max_num)
    #start with FIRST_PRIME (2) already established
    num_dict[FIRST_PRIME] = "prime"
    primes = [FIRST_PRIME]
    next_prime = FIRST_PRIME

    while next_prime < sqrt(max_num):
        next_prime = find_next_prime(next_prime, num_dict)
        num_dict = mark_multiples(next_prime, num_dict, max_num)

    return num_dict


def add_primes(num_dict):
    sum = 0

    for num in num_dict.keys():
        if num_dict[num] == "prime" or num_dict[num] == "":
            sum += num

    return sum


def calculate_answer():
    num_dict = get_primes(MAX_NUM)
    sum = add_primes(num_dict)

    print ("sum of primes below " + str(MAX_NUM) + " is " + str(sum) + ".")

if __name__ == "__main__":
    print("it took {} seconds to calculate this".format(timeit(stmt = calculate_answer, number = 1))) #result is 63.4923110008 seconds
#Currently I am using the Sieve of Eratosthenes
#I've read that the Sieve of Atkin is faster

