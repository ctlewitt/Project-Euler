#Initial ideas:
#There is probably a formula, since the square of the sums, if multiplied out (instead of added) includes the squares of the addends
#but the remaining products would form an obscenely long list to type out.
#Therefore, it is probably not worth looking up the formula and turning the nightmare into a program
#since brute force will probably not cost us much time, unfortunately

#IMPORT STATEMENTS...for some reason it's not importing correctly
#from prob1-multiples_of_3_and_5 import find_progression_sum

MAX = 100

#if import worked, would not need to paste def here
def find_progression_sum(occur):
#uses property that 1+num = 2+(num-2) = 3+(num-3) = ... so we don't need to use a for loop to add 1+2+3+...+num
#returns sum of 1+2+3+...+num
    if occur % 2 ==0: #even number of numbers
        summand = occur + 1
        total = summand * (occur/2)
    else: #odd number of numbers
        summand = occur
        total = summand * (occur/2 + 1)
    return total

def sum_of_squares(num):
#calcualtes the square of each number from 1 to num and adds them, returns sum
    sum = 0
    for num in range(1, MAX + 1):
        sum += num ** 2
    return sum

def square_of_sum(num):
#adds numbers from 1 to num and squares the sum, returns the square
    sum = find_progression_sum(num)
    square = sum ** 2
    return square


diff = square_of_sum(MAX) - sum_of_squares(MAX)
print diff