from math import sqrt
from mathfunctions.primes import get_primes
from timeit import timeit


MAX_NUM = 1000000
MAX_CHECK = sqrt(MAX_NUM)


# gets the number of prime rotations to be counted
# returns 0 if any rotations are not prime, otherwise returns number of unique rotations
def num_prime_rots_to_be_counted(prime, primes):
    prime_rots = get_prime_rotations(prime)
    for rot_prime in prime_rots:
        # check if rot_prime is prime
        if rot_prime not in primes or (primes[rot_prime] != "" and primes[rot_prime] != "prime"):
            return 0
        primes[rot_prime] = "already_checked"
    return len(prime_rots)


def get_prime_rotations(prime):
    prime_str = str(prime)
    prime_rots = set()
    for digit_idx in range(len(prime_str)):
        if prime_str[digit_idx] != "0":
            prime_rots.add(int(prime_str[digit_idx:]+prime_str[:digit_idx]))
    return prime_rots


def get_ans():
    primes = get_primes(MAX_NUM)
    num_circular_primes = 0
    for prime in list(primes.keys()):
        if primes[prime] == "" or primes[prime] == "prime":
            # check all rotations and add to count if appropriate
            num_circular_primes += num_prime_rots_to_be_counted(prime, primes)
    print(num_circular_primes)


if __name__ == "__main__":
    print("it took {} seconds to calculate this".format(timeit(stmt = get_ans, number = 1))) #result is 63.4923110008 seconds


