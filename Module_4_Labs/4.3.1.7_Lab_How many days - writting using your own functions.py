'''
Estimated Time
    15-20 minutes

Difficulty level
    Means

Requirements
    LABORATORY 4.1.3.6

Objectives
    Familiarize the student with:

        * Project and write parameterized functions.
        * Use instruction return.
        * Use the student's own functions.
        
Scenario
    Your task is to write and test a function that takes two arguments (one year and one month) and returns the number of days of the month/given year (while only February is sensitive to value year, your function should be universal).

    The initial part of the function is ready. Now make the function return None if the arguments don't make sense.

    Of course, you can (and should) use the previously written and tested function (LABORATORY 4.1.3.6). It can be very useful. We recommend that you use a list with the months. You can create it within the function; This trick will significantly shorten the code.

    We have prepared a test code. Expand it to include more test cases.
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
test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
	yr = test_years[i]
	mo = test_months[i]
	print(yr, mo, "->", end="")
	result = days_in_month(yr, mo)
	if result == test_results[i]:
		print("OK")
	else:
		print("Fallido")
