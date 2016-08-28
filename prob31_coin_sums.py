TOTAL = 200
COINS = [1, 2, 5, 10, 20, 50, 100]

def setup_memoize_array():
    coin_combos = [[1 if num == 0 else 0 for num in range(TOTAL + 1)] for _ in COINS]
    coin_combos[0] = [1 for _ in range(len(coin_combos[0]))]
    print(coin_combos)
    return coin_combos


def calculate_coin_combos():
    coin_combos = setup_memoize_array()
    for coin_idx, coin in enumerate(COINS):
        if coin_idx > 0: # don't do calculations for first row
            for amt in range(1, TOTAL + 1):
                temp_amt = amt - coin
                print(coin_combos[coin_idx][amt])
                coin_combos[coin_idx][amt] += coin_combos[coin_idx-1][amt]
                if amt >= coin:
                    coin_combos[coin_idx][amt] += coin_combos[coin_idx][amt-coin]
                # while temp_amt >= 0:
                #
                #     coin_combos[coin_idx][amt] += coin_combos[coin_idx][temp_amt]
                #     # coin_combos[coin_idx][amt] += coin_combos[coin_idx+1][temp_amt] ;actually this should be built into the larger coin amount
                #     temp_amt -= coin
    print(coin_combos)
    return coin_combos[len(COINS)-1][TOTAL]

print(calculate_coin_combos())


# sum = []
# sums = []
#
# def generate_empty_sum():
#     empty_sum = []
#     for i in range(len(COINS)):
#         empty_sum.append(0)
#     return empty_sum
#
# def shift_coin(sum_copy):
#     #find smallest demoniation place holder greater than 1pence with coins in it
#     i = -2
#     while sum_copy[i] == 0:
#         i -= 1 #THIS WILL BREAK WHEN EVERYTHING IS IN 1 PENCE POSITION!!!
#         if i == -(len(COINS) + 1):
#             return sum_copy
#     #break up 1 coin into largest possible denominations
#
#
#
#     sum_copy[i] -= 1 #remove 1 coin
#     coins_to_break = COINS[i] #calculate how much we are making change for
#     while coins_to_break != 0:
#         i += 1 #move one place value smaller
#         sum_copy[i] += coins_to_break / COINS[i] #give as many of this place value coins
#         coins_to_break = coins_to_break % COINS[i] #calculate remainder
#     return sum_copy
#
# for starting_position in range(0, len(COINS)):
# #for starting_position in range(0, 1):
#     sum = generate_empty_sum()
#     print sum
#     sum[starting_position] = TOTAL / COINS[starting_position]
#     print sum
#     while sum[starting_position] != 0:
#         print sum
#         sums.append(sum)
#         if starting_position == len(COINS) - 1:
#             break
#         sum = shift_coin(list(sum))
# #        pause = raw_input("press something")
#
# print len(sums)