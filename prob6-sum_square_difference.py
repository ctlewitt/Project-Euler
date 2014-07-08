#Initial ideas:
#There is probably a formula, since the square of the sums, if multiplied out (instead of added) includes the squares of the addends
#but the remaining products would form an obscenely long list to type out.
#Therefore, it is probably not worth looking up the formula and turning the nightmare into a program
#since brute force will probably not cost us much time, unfortunately

MAX = 100

def sum_of_squares(num):
#calcualtes the square of each number from 1 to num and adds them, returns sum
    #use for loop and range function
    pass
    
def square_of_sum(num):
#adds numbers from 1 to num and squares the sum, returns the square
    #use property that 1+num = 2+(num-2) = 3+(num-3) = ... so we don't need to use a for loop to them all up, then square
    pass

diff = square_of_sum(MAX) - sum_of_squares(MAX)
print diff
