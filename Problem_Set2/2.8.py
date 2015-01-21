__author__ = 'fhk'

# By Websten from forums
#
# Given your birthday and the current date, calculate your age in days.
# Account for leap days.
#
# Assume that the birthday and current date are correct dates (and no
# time travel).
#


daysOfMonths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
def isLeapYear(year):
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0

# print isLeapYear(2012)
# print isLeapYear(1900)
# print isLeapYear(2011)

def countDays(year, month, day):
    count = 0
    for m in range(0, month - 1):
        count = count + daysOfMonths[m]
    count = count + day
    if isLeapYear(year) and (month > 2 or month == 2 and day >= 29):
        count = count + 1
    return count

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    sum = 0
    if year2 == year1:
        sum = countDays(year2, month2, day2) - countDays(year1, month1, day1)
    else:
        sum = 365 - countDays(year1, month1, day1)
        if isLeapYear(year1):
            sum = sum + 1
        year1 = year1 + 1
        while year1 < year2:
            if isLeapYear(year1):
                sum = sum + 366
            else:
                sum = sum + 365
            year1 = year1 + 1
        sum = sum + countDays(year2, month2, day2)
    return sum

def test():
    test_cases = [((2012,1,1,2012,2,28), 58),
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523)]
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed"
        else:
            print "Test case passed!"

test()

