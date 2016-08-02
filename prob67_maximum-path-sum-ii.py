#python3.5.1
from time import time

start = time()

ROW = 0
COL = 1


# could probably optimize this better
def read_in_triangle(file_name):
    with open(file_name) as f:
        triangle = [[int(num) for num in line.split()] for line in f]
    return triangle


def find_greatest_paths_value(triangle):
    # go from bottom to top of triangle
    for row_idx in reversed(range(len(triangle)-1)):
        for col_idx in range(len(triangle[row_idx])):
            triangle[row_idx][col_idx] += max(triangle[row_idx+1][col_idx], triangle[row_idx+1][col_idx+1])
    return triangle[0][0]

triangle = read_in_triangle("prob67_triangle.txt")


print(find_greatest_paths_value(triangle))

end = time()

print("This program took %s seconds to run" %(end-start))
