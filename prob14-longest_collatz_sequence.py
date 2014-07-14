#initial thoughts:
#to save time: work from smallest to largest and create a dictionary of the results
#any time a sequence contains a number you've already calculated, just add the number of steps in the sub-sequence
#when doing an odd number starter, also save the larger even number's sequence that is produced
#e.g., 13 produces a subsequence of 40 (13*3+1=40), which has 1 fewer steps than the 13 sequence
#so, when starting an even number, always check if it's in the keys before calculating it

MAX = 1000000

def is_divisible(num, divisor):
#checks if number is divisible by divisor, returns True/False accordingly
    if num % divisor == 0:
        return True
    else:
        return False

sequence_steps = {}
sequence_steps[1] = 1
winner = [1, 1] #best [starter, steps]
starter_even = False
for starter in range(2, MAX):
    starter_even = not starter_even
    num = starter
    num_even = starter_even
    steps = 1
    if starter_even:
        if starter in sequence_steps.keys():
            print "starter: " + str(starter) + "already calculated: ",
            num = 1
            steps = sequence_steps[starter]
            print steps
    while num != 1:
        if num_even:
            num /= 2
            num_even = is_divisible(num, 2)
        else:
            num = 3*num + 1
            num_even = True
        steps += 1
        print "num: " + str(num) + " steps: " + str(steps)
        if num in sequence_steps.keys():
            steps += sequence_steps[num]
            print "starter: " + str(starter) + " already calculated: ",
            break

    sequence_steps[starter] = steps
    if steps > winner[1]:
        winner = [starter, steps]
        print "winner"
    if not starter_even:
        sequence_steps[3*starter+1] = steps - 1
        #since it's steps-1 steps, this should never be the max number of steps
        print "saved time: starter: " + str(starter) + " steps: " + str(steps)
print winner