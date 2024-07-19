'''
Estimated Time
    5 minutes

Difficulty level
    Very easy

Objectives
    * Become familiar with function input().
    * Become familiar with comparison operators in Python.
    
Scenario
    Using one of the comparison operators in Python, write a simple two-line program that takes the parameter n as input, which is an integer, and prints False Yes n is less than 100, and True Yes n is greater than or equal to 100.

    You should not create any block if (We will talk about them very soon). Test your code using the data we provide you.

Test Data

Entry example: 55
Expected result: False

Entry example: 99
Expected result: False

Entry example: 100
Expected result: True

Entry example: 101
Expected result: True

Entry example: -5
Expected result: False

Entry example: +123
Expected result: True
'''
# If the number is greater or equal to 100 the conditions is met (True) otherwise (False)
n = int(input("Enter a number (between 1 and 200: ")) >= 100
print(n)