TOTAL = 200
COINS = [1, 2, 5, 10, 20, 50, 100]

def setup_memoize_array():
    coin_combos = [[1 if num == 0 else 0 for num in range(TOTAL + 1)] for _ in COINS]
    coin_combos[0] = [1 for _ in range(len(coin_combos[0]))]
    return coin_combos


# O(num_denominations * amount_of_money)
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
    return coin_combos[len(COINS)-1][TOTAL]

print(calculate_coin_combos())
