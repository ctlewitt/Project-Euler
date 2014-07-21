#initialize variables
first_sundays = 0
days_in_month = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

#Jan 1, 1900 is a Monday.  Find Jan 1, 1901.
day_of_week = 1 #Monday
day_of_week = (day_of_week + 365) % 7 #1 non-leap year

#for 1901 to 2000, go through each month and count how many 1st are Sundays.  (2000 is a leap year b/c it's divisible by 400.)
for year in range(1901, 2001):
    if year % 4 ==0:
        days_in_month[2] = 29
    else:
        days_in_month[2] = 28
    for month in range(1, 13):
        if day_of_week == 0:
            first_sundays += 1
        day_of_week = (day_of_week + days_in_month[month]) % 7

print "first_sundays: " + str(first_sundays)