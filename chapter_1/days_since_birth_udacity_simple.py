months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """
    Calculates the number of days between two dates.
    """
    assert not isBefore(year2, month2, day2,
                        year1, month1, day1)

    days = 0
    while isBefore(year1, month1, day1, year2, month2, day2):
        year1, month1, day1 = nextDay(year1, month1, day1)
        days += 1
    return days


def isLeapYear(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True


def nextDay(year, month, day):
    """Simple version: assume every month has 30 days"""
    if day < daysInMonth(year, month):
        return year, month, day + 1
    else:
        if month == 12:
            return year + 1, 1, 1
        else:
            return year, month + 1, 1


def daysInMonth(year, month):
    daysInMonth = months[month - 1]
    if month == 2 and isLeapYear(year):
        daysInMonth += 1

    return daysInMonth


def isBefore(year1, month1, day1,
             year2, month2, day2):
    if year1 < year2:
        return True
    elif year1 == year2:
        if month1 < month2:
            return True
        elif month1 == month2:
            return day1 < day2
        else:
            return False
    else:
        return False


def test_daysInMonth():
    assert daysInMonth(2000, 2) == 29
    assert daysInMonth(2001, 2) == 28
    assert daysInMonth(2000, 1) == 31


def test_isLeapYear():
    assert isLeapYear(2000)
    assert not isLeapYear(1900)
    assert isLeapYear(1992)
    assert isLeapYear(1904)


def test_nextDay():
    assert nextDay(2018, 9, 3) == (2018, 9, 4)
    assert nextDay(2018, 12, 31) == (2019, 1, 1)
    assert nextDay(2018, 11, 30) == (2018, 12, 1)
    assert nextDay(2000, 2, 28) == (2000, 2, 29)
    assert nextDay(2000, 2, 29) == (2000, 3, 1)


def test_isBefore():
    assert isBefore(1991, 1, 1,
                    2019, 1, 1)

    assert isBefore(1991, 1, 1,
                    1991, 1, 2)

    assert not isBefore(1991, 1, 1,
                        1991, 1, 1)

    assert isBefore(1991, 1, 3,
                    1991, 2, 1)

    assert not isBefore(1992, 1, 3,
                        1991, 2, 1)


def test_DaysBetweenDates():
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
                             2019, 9, 2) == 10466)

    assert (daysBetweenDates(2012, 1, 1,
                             2013, 1, 1) == 366)

    print("Congratulations! Your daysBetweenDates")
    print("function is working correctly!")


test_daysInMonth()
test_isLeapYear()
test_nextDay()
test_isBefore()
test_DaysBetweenDates()
