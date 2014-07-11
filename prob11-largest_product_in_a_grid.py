def get_num_grid(file_name):
#reads file in and turns into list of lists
    num_grid = []
    with open(file_name) as f:
        for line in f:
            num_grid.append(line.split())
    return num_grid

#declare variables
    #grid = []
    #comparator = 0

num_grid = get_num_grid("prob11-number_grid.txt")

#determine width and height of grid using length of lists

#check and compare all products
    #check horizontal products
    #check vertical products
    #check diagonal, down to the right products
    #check diagonal, down to the left products






print num_grid