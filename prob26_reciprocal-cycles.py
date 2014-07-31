def find_repeat_length(divisor):
    remainders = []
    dividend = 1
    remainder = 1
    while remainder != 0:
        quotient = dividend / divisor #divide
        product = quotient * divisor #multiply
        remainder = dividend - product #subtract
        if remainder in remainders: #check if repeating decimal
            return len(remainders) - remainders.index(remainder)
        else: #add remainder to list for tracking repeating decimals
            remainders.append(remainder)
        dividend = remainder * 10 #"bring down a 0"
    return 0 #if not a repeating decimal

max_length = 0
max_i = 0

#check each number in 1/1 to 1/999 for its repeating decimal length
for i in range(1, 1000):
    repeat_length = find_repeat_length(i)
    if repeat_length > max_length:
        max_i = i
        max_length = repeat_length

#report results
print "The repeating fraction with the longest repeat is 1/" + str(max_i) + "."
print "Its repeat length is " + str(max_length) + " digits."
