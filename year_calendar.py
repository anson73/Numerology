
def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def getSum(n):
    sum = 0
    while (n != 0):
        sum = sum + (n % 10)
        n = n//10
    return sum

def reduce(n):
    if (n >= 0 and n <= 9) or (n == 11) or (n == 22) or (n == 33): 
        return n

    if n == 20: 
        return 11

    if n == 28: 
        return n

    return reduce(getSum(n))

def reduceMonth(month, year):
    reduce_month = month
    year_sum = getSum(year)

    # Version 1 (seperate digits month + year)
    month_V1 = month
    if month_V1 != 11:
        month_V1 = getSum(month_V1)

    month_V1 = reduce(month_V1 + year_sum)

    # Version 2 (whole month + year)
    month_V2 = reduce(month + year_sum)

    # Reduce month individually
    if reduce_month != 11:
        reduce_month = getSum(month)

    return (reduce_month, month_V1, month_V2)

def reduceDay(day, month, year):
    reduce_day = day
    year_sum = getSum(year)

    # Version 1 (seperate digits day + month + year)
    day_V1 = day
    if day_V1 != 11 and day_V1 != 22:
        # Reduce day individually
        if day_V1 == 20 or day_V1 == 29:
            reduce_day = 11
        else:
            reduce_day = reduce(day_V1)

        day_V1 = getSum(day_V1)

    month_V1 = month
    if month_V1 != 11:
        month_V1 = getSum(month_V1)

    day_V1 = reduce(day_V1 + month_V1 + year_sum)

    # Version 2 (whole day + month + year)
    day_V2 = reduce(day + month + year_sum)

    return (reduce_day, day_V1, day_V2)

months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

if __name__ == "__main__":
    year = int(input("Enter a year: "))

    isleapyear = is_leap_year(year)

    daycount = {1:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 11:0, 22:0, 33:0, 28:0}

    # Reduce the Year
    print(f"YEAR: {year} = {reduce(year)}")

    month = 1
    daynumber = 1
    for days in months:
        # Print months
        month_reduced, month_V1, month_V2 = reduceMonth(month, year)
        if month_V1 == month_V2:
            print(f"{month} : {month_reduced}, {month_V1}")
        elif month_V1 > month_V2:
            print(f"{month} : {month_reduced}, {month_V1}/{month_V2}")
        elif month_V1 < month_V2:
            print(f"{month} : {month_reduced}, {month_V2}/{month_V1}")
        
        # Check for leap year
        updateddays = days
        if month == 2 and isleapyear:
            updateddays += 1

        # Print Days
        day = 1
        while day <= updateddays:
            day_reduced, day_V1, day_V2 = reduceDay(day, month, year)
            if day_V1 == day_V2:
                print(f"\t{daynumber}) {day}/{month}/{year} : {day_reduced}, {day_V1}")
                daycount[day_V1] += 1
            elif day_V1 > day_V2:
                print(f"\t{daynumber}) {day}/{month}/{year} : {day_reduced}, {day_V1}/{day_V2}")
                daycount[day_V2] += 1
            elif day_V1 < day_V2:
                print(f"\t{daynumber}) {day}/{month}/{year} : {day_reduced}, {day_V2}/{day_V1}")
                daycount[day_V1] += 1

            day += 1
            daynumber += 1

        month += 1


