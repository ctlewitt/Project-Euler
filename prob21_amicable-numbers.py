MAX = 10000

def get_prime_factors(num):
    return prime_factors #dict
    pass

def get_sum_proper_divisors(prime_factors):
#get sum of factors of number (use primes, formula for sum of factors, subtract number (b/c sum includes number as factor.)
    return sum
    pass


num_dict = {} #num: sum of proper divisors]
for num in range(1, MAX+1):
    prime_factors = get_prime_factors(num, num_dict)
    sum_proper_divisors = get_sum_proper_divisors(prime_factors)
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