NUM_DIGITS = 4
OFFSET = NUM_DIGITS - 1

def get_num_grid(file_name):
#reads file in and turns into list of lists
    num_grid = []
    with open(file_name) as f:
        for line in f:
            num_grid.append(line.split())
    num_grid = turn_into_numbers(num_grid)
    return num_grid

def turn_into_numbers(num_grid):
    num_grid_copy = list(num_grid)
    for r_index, row in enumerate(num_grid_copy):
        for c_index, col in enumerate(row):
            num_grid[r_index][c_index] = int(col)
    return num_grid

def compare(max_product, product):
    if product > max_product:
        return product
    else:
        return max_product

def check_horizontal_products(num_grid, max_product):
    for row in num_grid:
        for col_index in range(grid_width-OFFSET):
            product = 1
            for cycler in range(NUM_DIGITS):
                product *= row[col_index + cycler]
            max_product = compare(max_product, product)
    return max_product

def check_vertical_products(num_grid, max_product):
    for col in range(grid_width):
        for row in range(grid_height-OFFSET):
            product = 1
            for cycler in range(NUM_DIGITS):
                product *= num_grid[row+cycler][col]
            max_product = compare(max_product, product)
    return max_product

def check_diagonal_dtr_products(num_grid, max_product):
    for row in range(grid_height-OFFSET):
        for col in range(grid_width-OFFSET):
            product = 1
            for cycler in range(NUM_DIGITS):
                product *= num_grid[row+cycler][col+cycler]
            max_product = compare(max_product, product)
    return max_product

def check_diagonal_dtl_products(num_grid, max_product):
    for row in range(grid_height-OFFSET):
        for col in range(OFFSET, grid_width):
            product = 1
            for cycler in range(NUM_DIGITS):
                product *= num_grid[row+cycler][col-cycler]
            max_product = compare(max_product, product)
    return max_product


#declare variables
max_product = 0
num_grid = get_num_grid("prob11-number_grid.txt")
grid_height = len(num_grid)
grid_width = len(num_grid[0])

#check and compare all products
max_product = check_horizontal_products(num_grid, max_product)
max_product = check_vertical_products(num_grid, max_product)
max_product = check_diagonal_dtr_products(num_grid, max_product)
max_product = check_diagonal_dtl_products(num_grid, max_product)


print "The largest product of " + str(NUM_DIGITS) + " sequential numbers in the grid is " + str(max_product) + "."
