from math import sqrt

BASENUMBER = 999
#change basenumber based on how many digits you want in your palindrome


def reverse_str(str):
#reverses a string. "123" becomes "321"
    rev_str = ""
    for letter in str:
        rev_str = letter + rev_str
    return rev_str

def create_palindrome(first_half_num):
#creates a palindrome from a number
# 123 becomes 123321
    str_num = str(first_half_num)
    rev_str_num = reverse_str(str_num)
    rev_num = int(rev_str_num)
    str_palindrome = str_num + rev_str_num
    palindrome = int(str_palindrome)
    return palindrome

def check_palindrome(palindrome):
#checks if palindrome is divisible by factor
#returns False if it is (so keep_trying = False)
#else True, so keep_trying = True
    factor = BASENUMBER
    keep_trying = True
    while factor > sqrt(palindrome) and keep_trying:
        if palindrome % factor == 0:
            keep_trying = False
        else:
            factor -= 1
    return keep_trying




#A different way of finding reverse_num for a 2 or 3 digit number
#put first_half_number in fromt of reverse_num for palindrome
#hundreds = first_half_num / 100
#tens = (first_half_num - hundreds*100) / 10
#units = first_half_num - hundreds*100 - tens*10

#if hundreds > 0:
#    reverse_num = units*100 + tens*10 + hundreds*1
#    palindrome = first_half_num*1000 + reverse_num
#else:
#    reverse_num = units*10 + tens*1
#    palindrome = first_half_num*100 + reverse_num


first_half_num = BASENUMBER + 1
#added 1 because I'm about to subtract it
#numbers should be "pal" and "indrome" so they can be "palindrome" when put together

keep_trying = True

while keep_trying:
    #down-increment number and generate new palindrome
    first_half_num -= 1
    palindrome = create_palindrome(first_half_num)
    #check palindrome
    keep_trying = check_palindrome(palindrome)

print palindrome

#MY LOGIC:
#999, 998, 997, 996, etc will find the greatest palindromes: 999999, 998899, 996699
#since we are looking for the largest product, we should begin by dividing by the largest (3 digit) factors
#a 6 digit number (e.g., 999999 divided by a 3 digit number, e.g., 999 will yield a 3 digit number
#we will only check each of the factors of a palindrome down to the square root,
#since the factors will swap which is greater/less, but will repeat values otherwise.