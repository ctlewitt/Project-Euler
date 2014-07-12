#THOUGHTS:
#loop through triangles and check factors, stopping when you have one with 500 factors
#If a triangle has >500 factors, it cannot have a value of <500 itself,
#so...I should start calculating factors only after I've reached a triangle with a number >500.
#But if we do 500 because it has 500 numbers below (and including it), we are assuming that the factors are dense in the whole numbers
#(ie, that every number below 500 is a factor of 500), which we know isn't true....
#so we can start calculating factors at a higher number.
#How high, thought.
#look at 500.  Factors come in pairs.  1 and 500, 2 and 250.  3 will have an even smaller partner-factor...,
#so we've skipped 249 numbers that could have been factors.  By that argument, we could up the starting number from 500 to 749.
#but let's be more forceful.  Let's start at 1000.  Factors include 1 and 1000, 2 and 500.  And right there, we've skipped 499 numbers.
#Assuming (although it's not possible) that numbers below .....(OH>>>>>I COULD BE MORE FORCEFUL!!!!) 500 are dense with factors,
#we could start at 999.  That's 500+1 factors, which is pretty close.  ....
#OKAY, but the more forceful version.  Factors come in pairs.  The first factor-partner is below the square root of the product/number.
#The second is above.  Assuming that we want 500 factors, 250 of them need below the square root.
#So. let's start calculating factors of numbers that are above the square of 250!  Yeah!!!!!!

#To calculate factors, I'll start by doing mods up to the square root, then I'll just divide the number by each known factor
#to find the rest of the factors.  Not optimal, but hopefully good enough given the previous optimization.

from math import sqrt

def get_next_triangle(counter, triangle):
    next_triangle = triangle + counter
    return next_triangle

def find_num_factors(triangle):
    factor = 1
    factors = []
    while factor <= sqrt(triangle):
        if triangle % factor == 0:
            factors.append(factor)
        factor += 1
    for factor in factors:
        factor_partner = triangle / factor
        factors.append(factor_partner)
    return len(factors)



#OUTLINE:
MIN_FACTORS = 500
counter = 0
triangle = 0
while triangle < (MIN_FACTORS/2)**2:
    counter += 1
    triangle = get_next_triangle(counter, triangle)
    print "tri: " + str(triangle)

still_looking = True
while still_looking:
    counter += 1
    triangle = get_next_triangle(counter, triangle)
    print "tri: " + str(triangle)
    num_factors = find_num_factors(triangle)
    print "num_factors: " + str(num_factors)
    if num_factors >= 500:
        still_looking = False
print "The first triangle with over 500 factors is " + str(triangle) + "."