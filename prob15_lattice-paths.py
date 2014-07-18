from time import time

start = time()
DIM = 6


def add_col(size):
#returns sum of the numbers 1, 2, 3, ..., size.
    col = 0
    for num in range(1, size + 1):
        col += num
    return col


def add_triangle(size):
#returns sum of columns of size: 1, 2, 3, ..., size-2, size-1, size
#e.g., (1) + (1+2) + (1+2+3) + (1+2+3+4) + (1+2+3+4+5)
    triangle = 0
    for num in range(1, size+1):
        triangle += add_col(num)
    return triangle


def add_triangle_progression(size):
#returns sum of triangles of size: 1, 2, 3, ..., size-2, size-1, size
    progression = 0
    for num in range(1, size+1):
        progression += add_triangle(num)
    return progression


def add_reducing_triangle_progressions(size):
#returns sum of triangle progressions starting with triangles of sizes: 1, 2, 3, ..., size-2, size-1, size
#in the program, it's expanding triangle progressions, but in reality (in the paths), they reduce from size down to 1.
    reducing_progression = 0
    for num in range(1, size+1):
        reducing_progression += add_triangle_progression(num)
    return reducing_progression


paths = 0
step = 1

#step 1) 1
if DIM+1 >= step:
    paths += 1
    print "step:" + str(step)
    print "paths:" + str(paths)
    step += 1

#step 2) dim
if DIM+1 >= step:
    paths += DIM
    print "step:" + str(step)
    print "paths:" + str(paths)
    step += 1


#step 3) 1 to dim
if DIM+1 >= step:
    paths += add_col(DIM)
    print "step:" + str(step)
    print "paths:" + str(paths)
    step += 1

#step 4) dim-triangle
if DIM+1 >= step:
    paths += add_triangle(DIM)
    print "step:" + str(step)
    print "paths:" + str(paths)
    step += 1

#step 5) 1-triangle to dim-triangle
if DIM+1 >= step:
    paths += add_triangle_progression(DIM)
    print "step:" + str(step)
    print "paths:" + str(paths)
    step += 1

#steps 6 to DIM+1) {1-triangle to dim-triangle}, {1-triangle to (dim-1)-triangle}, ..., {1-triangle}
multiplier = 1
while DIM+2 >= step:
    paths += add_reducing_triangle_progressions(DIM)
    print "step:" + str(step)
    print "paths:" + str(paths)
    step += 1

print "There are %s possible paths you can take to traverse a %s by %s lattice." %(paths, DIM, DIM)

end = time()
print "it took %s seconds" %(end-start)

#quick test
test = 0
for num in range(1, 22):
    test += num * (DIM +2 - num)
    print str(test) + "=" + str(num) + "*" + str(DIM+2-num)
print "test" + str(test)