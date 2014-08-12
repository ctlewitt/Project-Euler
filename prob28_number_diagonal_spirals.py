from timeit import timeit


MAX_DIM = 1001
JUMPER  = 8
MAX_SQUARE = MAX_DIM ** 2

def method1():
    square_ave = 6
    spacer = 5
    sum = 0

    while square_ave < MAX_SQUARE:
        sum += square_ave
        spacer += JUMPER
        square_ave += spacer

    sum *= 4
    sum +=1

    print "Method1: the sum of the corners is " + str(sum)


#second way.  to see which is more efficient.

def average_corners(n):
    return 1+(5*n)+4*(n**2-n)

def method2():
    sum = 0

    for counter in range(1,501):
        sum += average_corners(counter)

    sum *= 4
    sum += 1

    print "Method2: the sum of the corners is " + str(sum)


print timeit(stmt = method1, number = 1) #result is 63.4923110008 seconds
print timeit(stmt = method2, number = 1) #result is 63.4923110008 seconds
