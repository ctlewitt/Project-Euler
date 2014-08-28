POWER = 5

def create_power_dict(power):
    power_dict = {}
    for num in range(0, 10):
        power_dict[num] = num ** power
    return power_dict

def get_max_check(power):
    counter = 1
    while (9 ** power) * counter >= int("9" * counter):
        counter += 1
    max_check = (9 ** power) * (counter - 1)
    return max_check

def check_power_sum(num, power_dict):
    sum = 0
    for digit in str(num):
        sum += power_dict[int(digit)]
    if sum == num:
        return True
    else:
        return False


power_dict = create_power_dict(POWER)
power_sum_total = 0

max = get_max_check(POWER)
print max
for num in range(10, max+1):
    is_power_sum = check_power_sum(num, power_dict)
    if is_power_sum:
        print num
        power_sum_total += num

print power_sum_total
