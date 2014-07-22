from string import ascii_uppercase

def generate_letter_values():
    letter_values = {}
    for value, letter in enumerate(ascii_uppercase, start = 1):
        letter_values[letter] = value
    return letter_values

def name_letters_value(name, letter_values):
    name_value = 0
    for letter in name:
        name_value += letter_values[letter]
    return name_value


def get_names(file_name):
#reads file in and turns into list
    names = []
    with open(file_name) as f:
        for line in f:
            names= line.split('","')
    names[0] = names[0].lstrip('"')
    names[-1] = names[-1].rstrip('"')
#    num_grid = turn_into_numbers(num_grid)
    return names


#read in names, save as list
names = get_names("prob22_names.txt")
#create dictionary of values for each letter
letter_values = generate_letter_values()

#sort names into alphabetical order
names.sort()

#calculate total score by adding up the products of each name's rank and letter_values.
total_score = 0
for order_rank, name in enumerate(names, start=1):
    total_score += order_rank*name_letters_value(name, letter_values)
print total_score
