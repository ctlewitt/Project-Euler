#initial thoughts:
#to save time: work from smallest to largest and create a dictionary of the results
#any time a sequence contains a number you've already calculated, just add the number of steps in the sub-sequence
#when doing an odd number starter, also save the larger even number's sequence that is produced
#e.g., 13 produces a subsequence of 40 (13*3+1=40), which has 1 fewer steps than the 13 sequence
#so, when starting an even number, always check if it's in the keys before calculating it

import time
start = time.time()
MAX = 1000000

def is_divisible(num, divisor):
#checks if number is divisible by divisor, returns True/False accordingly
    if num % divisor == 0:
        return True
    else:
        return False

def collatz_sequence(n_temp):
    #check if repeat number
#        if is_even == False:
#            if n_temp*2 not in collatz.keys(): ADD BACK IN TO SEE IF FASTER
#            collatz[n_temp*2] = collatz[n_temp] + 1
    mini_collatz = [n_temp]
    seq_len = 1
    while n_temp > 1:
        #find next number in sequence
        if is_divisible(n_temp, 2):
            n_temp /= 2
        else:
            n_temp = 3 * n_temp + 1
        #decide if next number is new. if new, add it and proceed.  if not new, use old data and stop
#        if n_temp in collatz.keys():
#            seq_len += collatz[n_temp]
#            break
#        else:
#            mini_collatz.append(n_temp)
        seq_len += 1
    return mini_collatz, seq_len

MAX = 1000000
HALF_MAX = MAX/2
is_even = False
collatz = {}
max = [1,1] #[starting_number, sequence_length]
#skip_list = range(6)

skipper = 1

#for n in range(HALF_MAX, MAX):
for n in range(HALF_MAX, MAX):
    #cycle i
    if skipper < 5:
        skipper += 1
    else:
        skipper = 0

    if skipper not in [2, 4, 5]: #takes care of 4(mod6) and 2(mod3) cases.
        #see this page for explanation http://math.stackexchange.com/questions/60573/reducing-the-time-to-calculate-collatz-sequences
        #if already done, skip
#        if n not in collatz.keys():
        mini_collatz, seq_len = collatz_sequence(n)
        #enter in steps for each number in sequence to save time later
        collatz[n] = seq_len



        #for i, num in enumerate(mini_collatz):
        #    collatz[num] = seq_len - i
        #check for new max sequence length
        if seq_len > max[1]:
            max = [mini_collatz[0], seq_len]

elapsed = (time.time() - start)
print "The longest sequence starts with %s and is %s digits long. \nIt took %s second to find the solution" % (max[0], max[1], elapsed)