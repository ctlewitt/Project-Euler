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

def collatz_sequence(n_temp, collatz):
    #check if repeat number
    if n_temp in collatz:
#        if is_even == False:
#            if n_temp*2 not in collatz.keys(): ADD BACK IN TO SEE IF FASTER
#            collatz[n_temp*2] = collatz[n_temp] + 1
        return [n_temp], collatz[n_temp]
    else:
        mini_collatz = [n_temp]
        seq_len = 1
        while n_temp != 1:
            #find next number in sequence
            if is_divisible(n_temp, 2):
                n_temp /= 2
            else:
                n_temp = 3 * n_temp + 1
            #decide if next number is new. if new, add it and proceed.  if not new, use old data and stop
            if n_temp in collatz.keys():
                seq_len += collatz[n_temp]
                break
            else:
                mini_collatz.append(n_temp)
                seq_len += 1
#            print "n_temp: ",
#            print n_temp
#    print "mini_collatz:",
#    print mini_collatz
    return mini_collatz, seq_len

MAX = 1000000
HALF_MAX = MAX/2
is_even = False
collatz = {}
for n in range(333333, MAX):
    mini_collatz, seq_len = collatz_sequence(n, collatz)
    for i, num in enumerate(mini_collatz):
        collatz[num] = seq_len - i
    #if the starting number is odd, the sequence starting with double that number has one more number

    if n <= HALF_MAX:
        collatz[n*2] = seq_len + 1

max = [1,1]
for n in collatz.keys():
    if collatz[n]>max[1]:
        max = [n, collatz[n]]

print collatz
print max
print collatz[910107]

#for each number in the list
#for each odd number, double the starter and add 1 number to the steps
