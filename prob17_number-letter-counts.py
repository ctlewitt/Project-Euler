def get_len_words(word_list):
    length = 0
    for word in word_list:
        length += len(word)
    return length

units = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
tens = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

hundreds = []
for unit in units:
    hundreds.append(unit +"hundredand")
#hundreds = ["onehundredand", "twohundredand", ..., "ninehundredand"]
len_numbers = 0

#get length of units numbers (1-9)
len_units = get_len_words(units)

len_numbers += len_units

#get length of numbers 10-99
#10 to 19
len_tens = get_len_words(teens)
#20 to 99
for ten in tens:
    len_tens += 10 * (len(ten)) + len_units

len_numbers += len_tens

#100-999
len_hundreds = 0
for hundred in hundreds:
    len_hundreds += 100*(len(hundred)) - len("and")
    len_hundreds += len_units + len_tens

len_numbers += len_hundreds

#1000
len_numbers += len("onethousand")

print len_numbers

######
#another way:
units_length = get_len_words(units)
teens_length = get_len_words(teens)
tens_length = get_len_words(tens)
hundreds_length = get_len_words(hundreds)

answer = 0
answer += 10*9*units_length
answer += 10*teens_length
answer += 10*10*tens_length
answer += 100*hundreds_length
answer += len("onethousand")
answer -= 9*len("and")
print answer