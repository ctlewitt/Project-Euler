
#Something tells me it won't be this simple....based on number size....
#If it's not....
#Maybe I only need to add up the beginnings of the numbers
#How many extra digits would I need?
#How long does it take for "carrying" to propagate?
#We are adding numbers 100 times, after all....


def get_nums_from_file(file_name):
#reads file in and turns into list of lists
    nums = []
    with open(file_name) as f:
        for line in f:
            nums.append(long(line.strip("\n")))
            #might need to make them be "long"s
    return nums

def get_total(nums):
    sum = 0
    for num in nums:
        sum += num
    return sum

nums = get_nums_from_file("prob13-100-50-digit-numbers.txt")
sum = get_total(nums)
#slice the first 10 digits of sum, turning it into a string first
first_ten_digits = str(sum)[:10]
print "first ten digits of sum: " + str(first_ten_digits)
