#testing work with 2 digit numbers and 4 digit palindrome products
#later, the project will be 3 digit numbers and 9 digit palindrome products

num1 = 99
num2 = 99

first_half_num = 99


#find reverse_num
#put first_half_number in fromt of reverse_num for palindrome
hundreds = first_half_num / 100
tens = (first_half_num - hundreds*100) / 10
units = first_half_num - hundreds*100 - tens*10

if hundreds > 0:
    reverse_num = units*100 + tens*10 + hundreds*1
    palindrome = first_half_num*1000 + reverse_num
else:
    reverse_num = units*10 + tens*1
    palindrome = first_half_num*100 + reverse_num

#check divisible #but only check while first num > second num

#if not divisible, increment first_half_num down and redo

#99, 98, 97, 96, etc will find the greatest palindromes: 9999, 9889, 9669
#since we are looking for the largest product, we should begin by dividing by the largest (2 digit) integers
