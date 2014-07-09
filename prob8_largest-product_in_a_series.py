def get_num_string(file_name):
    num_str = ""
    with open(file_name) as f:
        for line in f:
            num_str += line
    return num_str

#num_digits = 13
#comparator = 0
#read in number
#product = product of first 13 digits
#if product > comparator:
    #comparator = product
#get next digit (append to mini list)
#if first_digit != 0:
    #product /= first_digit
    #product *= next_digit
#else:
    #product = product of 13 current digits

num_string = get_num_string("prob8_number-series.txt")
print num_string
print
print num_string [:13]
print
print num_string [-13:]
