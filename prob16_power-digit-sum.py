import time

start = time.time()

num = 2**1000
num_str = str(num)
sum = 0
for char in num_str:
    sum += int(char)

print sum
time_elapsed = time.time() - start
print "it took " + str(time_elapsed) + " seconds."