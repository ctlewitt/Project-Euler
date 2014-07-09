from math import sqrt

SUM = 1000 #because a+b+c=1000

#Find solution
solutions = []
found_solution = False
for a in range(1, SUM):
    for b in range(a + 1, SUM):
        c = SUM - (a + b)
        if c > b:
            hypoten = sqrt(a**2 + b**2)
            if c == hypoten:
                found_solution = True
                solutions.append([a, b, c])
                
#Print solution
if found_solution:
    print "solutions:"
    for solution in solutions:
        for i, variable in enumerate(["a","b","c"]):
            print variable + " = " + str(solution[i])
        print "a*b*c = " + str(solution[0]*solution[1]*solution[2])