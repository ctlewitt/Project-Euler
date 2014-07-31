#Not correct. Just testing formulas to see what they're like

def calculate_primes(a, b):
    primes = []
    for n in range(50):
        primes.append(n**2 + a*n + b)
    print primes
    return

for a in range(-10, 10):
    for b in range(-10, 10):
        print "a=" + str(a)
        print "b=" + str(b)
        calculate_primes(a, b)