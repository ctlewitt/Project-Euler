from mathfunctions.primes import get_primes
from math import sqrt
from timeit import timeit



MAX_NUM= 2000000
MAX_CHECK = sqrt(MAX_NUM)



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

