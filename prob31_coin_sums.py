TOTAL = 200
COINS = [100, 50, 20, 10, 5, 2, 1]

sum = []
sums = []

def generate_empty_sum():
    empty_sum = []
    for i in range(len(COINS)):
        empty_sum.append(0)
    return empty_sum

def shift_coin(sum_copy):
    #find smallest demoniation place holder greater than 1pence with coins in it
    i = -2
    while sum_copy[i] == 0:
        i -= 1 #THIS WILL BREAK WHEN EVERYTHING IS IN 1 PENCE POSITION!!!
        if i == -(len(COINS) + 1):
            return sum_copy
    #break up 1 coin into largest possible denominations



    sum_copy[i] -= 1 #remove 1 coin
    coins_to_break = COINS[i] #calculate how much we are making change for
    while coins_to_break != 0:
        i += 1 #move one place value smaller
        sum_copy[i] += coins_to_break / COINS[i] #give as many of this place value coins
        coins_to_break = coins_to_break % COINS[i] #calculate remainder
    return sum_copy

for starting_position in range(0, len(COINS)):
#for starting_position in range(0, 1):
    sum = generate_empty_sum()
    print sum
    sum[starting_position] = TOTAL / COINS[starting_position]
    print sum
    while sum[starting_position] != 0:
        print sum
        sums.append(sum)
        if starting_position == len(COINS) - 1:
            break
        sum = shift_coin(list(sum))
#        pause = raw_input("press something")

print len(sums)