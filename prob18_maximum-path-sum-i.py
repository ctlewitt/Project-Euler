from time import time

#I know this isn't the most elegant solution, but it is my first program that uses recursion, and I'm really proud!!!  :)

start = time()

ROW = 0
COL = 1
#last_position = [row, col]

def read_in_triangle(file_name):
    triangle = []
    with open(file_name) as f:
        for line in f:
            mini_list = line.split()
            triangle.append(mini_list)
    triangle = turn_into_numbers(triangle)
    return triangle

def turn_into_numbers(str_list):
    num_list = []
    for mini_str_list in str_list:
        mini_num_list = []
        for str_num in mini_str_list:
            mini_num_list.append(int(str_num))
        num_list.append(mini_num_list)
    return num_list

def find_all_paths(current_path, last_position, triangle, all_paths):
    if last_position[ROW] == len(triangle) - 1:
        all_paths.append(current_path)
        return current_path
    else:
        current_path0 = list(current_path)
        current_path1 = list(current_path)

        next_position0 = [last_position[ROW] + 1, last_position[COL]]
        next_position1 = [last_position[ROW] + 1, last_position[COL] + 1]

        current_path0.append(triangle[next_position0[ROW]][next_position0[COL]])
        current_path1.append(triangle[next_position1[ROW]][next_position1[COL]])

        find_all_paths(current_path0, next_position0, triangle, all_paths)
        find_all_paths(current_path1, next_position1, triangle, all_paths)

#get triangle
triangle = read_in_triangle("prob18_triangle.txt")

#initialize variables
all_paths = []
current_path = []
#starting position and first partial current_path (made of starting position in triangle)
position = [0, 0]
current_path.append(triangle[0][0])

#find all paths in triangle (recursive function)
find_all_paths(current_path, position, triangle, all_paths)

#find path whose members have the highest sum
sum = 0
max = 0
winner = []
for path in all_paths:
    sum = 0
    for step in path:
        sum += step
    if sum > max:
        max = sum
        winner = path

end = time()

#report back
print "winning path: " + str(winner)
print "maximum sum of path steps: " + str(max)
print "This program took %s seconds to run" %(end-start)
