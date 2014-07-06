max = 1000 - 1
num1 = 3
num2 = 5
prod = num1 * num2

def find_progression_sum(occur):
    if occur % 2 ==0:
        summand = occur + 1
        total = summand * (occur/2)
    else:
        summand = occur
        total = summand * (occur/2 + 1)
    return total

def find_sum_of_multiples(num, max):
    occur = max/num
    total = num*find_progression_sum(occur)
    return total

prog1_total = find_sum_of_multiples(num1, max)
prog2_total = find_sum_of_multiples(num2, max)
common_multiples_total = find_sum_of_multiples(prod, max)

sum_of_multiples = prog1_total + prog2_total - common_multiples_total

print sum_of_multiples

