def find_repeat_length(i):
    #divide 1 by i, long division style, myself
    #keep a list of each variable at any given point
    #dividend, quotient, remainder
    #check if all 3 repeat
    #find number of steps taken since then, not counting the current one
    pass

def test_for_repeat(i):
    repeats = True
    division = 1/i
    if len(str(division)) < 10000:
        repeats = False
    return repeats

max_length = 0

for i in range(1, 1001):
    is_repeat = test_for_repeat(i)
    if is_repeat:
        length = find_repeat_length(i)
        if length > max_length:
            max_length = length
            max_i = i

print max_i
