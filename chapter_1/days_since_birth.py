months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """
    Calculates the number of days between two dates.
    """

    if year1 == year2 and month1 == month2 and day1 == day2:
        return 0
    elif year1 == year2 and month1 == month2:
        return day2 - day1
    elif year1 == year2:
        days_old = months[month1 - 1] - day1
        days_old += day2
        for i in range(month1 + 1, month2 - 1):
            days_old += months[i]

        return days_old
    else:
        # add the days until the end of the starting month
        days_old = months[month1 - 1] - day1

        # add the days until the end of the starting year
        for i in range(month1, len(months)):
            days_old += months[i]

        # add the days for each year, checking if it's a leap year,
        # the range is as follows: the first year is the year after
        # the starting year and the last year is the one before the
        # the current year
        for year in range(year1 + 1, year2):
            days_old += 365
            if is_leap_year(year):
                days_old += 1

        if is_leap_year(year2 + 1) and month2 > 1:
            days_old += 1

        for i in range(0, month2 - 1):
            days_old += months[i]

        days_old += day2

        return days_old


def is_leap_year(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True


def testDaysBetweenDates():
    # test same day
    assert (daysBetweenDates(2017, 12, 30,
                             2017, 12, 30) == 0)

    # test adjacent days
    assert (daysBetweenDates(2017, 12, 30,
                             2017, 12, 31) == 1)
    # test new year
    assert (daysBetweenDates(2017, 12, 30,
                             2018, 1, 1) == 2)
    # test full year difference
    assert (daysBetweenDates(2012, 6, 29,
                             2013, 6, 29) == 365)

    assert (daysBetweenDates(1991, 1, 6,
                             2019, 9, 2) == 10467)

    print("Congratulations! Your daysBetweenDates")
    print("function is working correctly!")


testDaysBetweenDates()
