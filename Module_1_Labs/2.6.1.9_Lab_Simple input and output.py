'''
Estimated Time
    5-10 minutes

Difficulty level
    Easy

Objectives
    * Become familiar with data entry and exit in Python.
    * Evaluate simple expressions.
    
Scenario
    The task is to complete the code to evaluate and display the result of four basic arithmetic operations.

    The result must be displayed in console.

    You may not be able to protect the code of a user trying to divide by zero. For now, no need to worry about it.

    Test your code - Does it produce the expected results?

    We will not show you any test data, that would be too simple.
'''
# enter a floating value for the variable a here
a = float(input("Enter a number: "))
# enter a floating value for the variable b here
b = float(input("Enter another number: "))

# show the result of the sum here 
print(f"The sum of 'a' and 'b' is: {a + b}")
# show the result of the substraction here
print(f"The substraction of 'a' and 'b' is: {a - b}")
# show the result of the multiplication here
print(f"The multiplication of 'a' and 'b' is: {a * b}")
# show the result of the division here
print(f"The division of 'a' and 'b' is: {a / b}")

print("\nThat's it, folks!")