'''
Estimated Time
    20-30 minutes

Difficulty level
    Means

Requirements
    LABORATORY 4.1.3.6
    LABORATORY 4.1.3.7

Objectives
    Familiarize the student with:

        * Project and write functions with parameters.
        * Use the sentence return.
        * Build a set of utility functions.
        * Use the student's own functions.
        
Scenario
    Your task is to write and test a function that takes three arguments (one year, one month, and one day of the month) and returns the corresponding day of the year, or returns None if any of the arguments is invalid.

    You must use previously written and tested functions. Add some test cases to the code. This test is only the beginning.
'''
#  -----------------------------------  #
#  L E A P   Y E A R   F U N C T I O N
#  -----------------------------------  #
def is_year_leap(year):
    if year >= 1582:
        if (year % 4 ) != 0:
            return False         # Common year
        elif (year % 100) != 0:
            return True          # Leap year
        elif (year % 400 ) != 0:
            return False         # Common year
        else:
            return True          # Leap year

#  -------------------------------------------  #
#  D A Y S   I N   M O N T H   F U N C T I O N
#  -------------------------------------------  #
def days_in_month(year, month):
    if year < 1582 or month < 1 or month > 12 :
        return None
    
    
    days = {
        '1':31,      # Jan
        '2':28,      # Feb
        '3':31,      # Mar
        '4':30,      # Apr
        '5':31,      # May
        '6':30,      # Jun
        '7':31,      # Jul
        '8':31,      # Aug
        '9':30,      # Sep
        '10':31,     # Oct
        '11':30,     # Nov
        '12':31}     # Dec
    
    if month == 2 and is_year_leap(year) :
        return 29
    else :
        return days[str(month)]

#  -----------------------  #
#  C A L C U L A T I O N S
#  -----------------------  #
def day_of_year(year, month, day):
    days = 0
    
    for actual_month in range(1,month) :
        aux = days_in_month(year,actual_month)
        days+= aux
    days +=day
    return days

print(day_of_year(2000, 2, 1))

print(day_of_year(2000, 12, 31))