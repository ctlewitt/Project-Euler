#declare variables
    #grid = []
    #comparator = 0

#take in file
    #read in each row
    #turn row into list of numbers
    #append each list onto list of lists to form "grid"

#determine width and height of grid using length of lists

#check and compare all products
    #check horizontal products
    #check vertical products
    #check diagonal, down to the right products
    #check diagonal, down to the left products


def get_num_grid(file_name):
    num_grid = []
    with open(file_name) as f:
        for line in f:
            num_grid.append(line.split())
    return num_grid


num_grid = get_num_grid("prob11-number_grid.txt")

print num_grid