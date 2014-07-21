def read_in_triangle(file_name):
    triangle = []
    mini_list = []
    with open(file_name) as f:
        for line in f:
            mini_list = line.split()
            print mini_list
            triangle.append(mini_list)
    print triangle
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

triangle = read_in_triangle("prob18_triangle.txt")
num_count = 0
sum = 0
for row in triangle:
    for col in row:
        num_count += 1
        sum += col

print sum
print num_count
print "average number: " + str(sum/num_count)