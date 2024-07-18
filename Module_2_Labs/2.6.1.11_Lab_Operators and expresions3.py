'''
Estimated Time
    15-20 minutes

Difficulty level
    Easy

Objectives
    * Improve the ability to implement numbers, operators, and arithmetic operations in Python.
    * Use function print() and its formatting capabilities.
    * Learn to express day-to-day phenomena in terms of a programming language.
    
Scenario
    The task is to prepare a simple code to evaluate or find the end time of a given period of time, expressing it in hours and minutes. Hours range from 0 to 23 and minutes from 0 to 59. The result must be displayed on the console.

    For example, if the event starts at 12:17 and hard 59 minutes, will end at 13:16.

    Do not worry if your code is not perfect, it is fine if you accept an invalid time, the most important thing is that the code produces a correct output according to the given entry.

    Test the code carefully. Track: use the operator % can be key to success.

Test Data
    Sample input:
        12
        17
        59

        Expected departure: 13:16


    Sample input:
        23
        58
        642

            Expected departure: 10:40   


    Sample input:
        0
        1
        2939

            Expected departure: 1:0
'''
# ------------------------
# code your test data here
# ------------------------
hour = int(input("Starting hour (Hour): "))
mins = int(input("Starting minute (minutes): "))
duration = int(input("Duration of the event in minutes: "))

# ------------------------
# write your code here
# ------------------------
hour += (((mins + duration) // 60) % 24)
mins = int((mins + duration) % 60 )


# Validate results
print(f"{hour}:{mins}")
        