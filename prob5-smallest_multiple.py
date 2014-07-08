#Initial ideas:
#Keep a prime factor dictionary for the lowest common multiple
#Use dictionaries to keep track of the prime factors for each number
#Every additional prime factor that isn't already in the LCM dictionary needs to be added to it


def find_prime_factors(num):
#returns dictionary of prime factors of num
    pass
  
def update_lcm_factors(lcm_factors, num_factors):
#returns updated lcm_factors with any additional factors from num_factors
    pass

def find_product(lcm_factors):
#returns the product of all the prime factors contained in dictionary
    pass


lcm_factors = {}
for num in range(MAX_NUMBER):
    num_factors = find_prime_factors(num)
    lcm_factors = update_lcm_factors(lcm_factors, num_factors)

lcm = find_product(lcm_factors)
print lcm
