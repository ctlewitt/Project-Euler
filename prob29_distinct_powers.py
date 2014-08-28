MIN = 2
MAX = 100

powers = set()

for a in range(MIN, MAX+1):
    for b in range(MIN, MAX+1):
        powers.add(a ** b)

print len(powers)