from itertools import permutations

numbers = range(0, 10)
permuted_nums = list(permutations(numbers))
print permuted_nums[999999]
