STR_LEN = 13

def get_num_string(file_name):
    num_str = ""
    with open(file_name) as f:
        for line in f:
            num_str += line.strip("\n")
    return num_str

def get_next_substring(string, i):
    good_substring = False
    skipped = False
    substring = ""
    while not good_substring:
        substring = string[i:i+STR_LEN]
        good_substring = True
        if "0" in substring:
            i += substring.index("0") + 1
            good_substring = False
            skipped = True
    return substring, i, skipped

def get_product_skipped(string):
    if "0" in string:
        return 0
    else:
        product = 1
        for char in string:
            product *= int(char)
        return product

def get_product(string, product, last_num):
    product = (product/int(last_num))*int(string[-1])
    return product

num_string = get_num_string("prob8_number-series.txt")
#read in number
comparator = 0
best_numbers = ""
product = 1
i = 0

#initial case
substring, i, skipped = get_next_substring(num_string, i)
product = get_product_skipped(substring)
i += 1

while i < len(num_string) - STR_LEN:
    substring, i, skipped = get_next_substring(num_string, i)
    if skipped:
        product = get_product_skipped(substring)
        skipped = False
    else:
        product = get_product(substring, product, num_string[i-1])
    if product > comparator:
        comparator = product
        best_numbers = substring
    i += 1


print comparator