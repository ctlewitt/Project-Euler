NUM = 5

sums = []
sum = []
running_total = 0




sums = []
for num in reversed(range(1, NUM)):
    sum = [num]
    running_total = num
    diff = NUM - num
    if diff < num:
        sum.append(diff)
        running_total += diff
    else:
        sum.append(num)
        running_total += num
        diff = NUM - running_total
        if running_total < NUM:
            if diff < sum[-1]:
                sum.append(diff)
                running_total += diff
            else:
                sum.append(sum[-1])
                running_total += sum[-1]
                diff = NUM - running_total
    sums.append(sum)

print sums