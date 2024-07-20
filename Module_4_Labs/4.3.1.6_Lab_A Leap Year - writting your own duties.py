'''
Estimated Time
    10-15 minutes

Difficulty level
    Easy

Objectives
    Familiarize the student with:

        * Project and write functions with parameters.
        * Use instruction return.
        * Test the functions.
Scenario
    Your task is to write and test a function that takes an argument (one year) and returns True if the year is a leap year, or False if it is not.

    Part of the skeleton of the function is already in the editor.

    Note: We have also prepared a short test code, which you can use to test your function.

    The code uses two lists: one with the test data and the other with the expected results. The code will tell you if any of your results are invalid.
'''
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

test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]
for i in range(len(test_data)):
	yr = test_data[i]
	print(yr,"->",end="")
	result = is_year_leap(yr)
	if result == test_results[i]:
		print("OK")
	else:
		print("Fallido")
