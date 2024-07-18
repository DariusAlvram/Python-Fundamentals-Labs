'''
Estimated Time
    10-15 minutes

Difficulty level
    Easy

Objectives
    * Become familiar with the concepts of numbers, operators, and arithmetic operations in Python.
    * Perform basic calculations.
Scenario
    Look at the code in the editor: read a value flotante, places it in a variable called x, and prints the value of the variable called y. Your task is to complete the code to evaluate the following expression:

        3x^3 - 2x^2 + 3x - 1

    The result must be assigned to y.

    Remember that classical algebraic notation very often omits the multiplication operator, here it must be explicitly included. Notice how the data type is changed to make sure that x is of the type flotante.

    Keep your code clean and readable, and test it using the data that has been provided. Don't be discouraged by not doing it on the first try. Be persistent and curious.


Test Data
    Sample Entry

        x = 0
        x = 1
        x = -1

    Expected departure

        y = -1.0
        y = 3.0
        y = -9.0
'''
# ------------------------
# code your test data here
# ------------------------
x =  [0, 1, -1]
expected_res = [-1.0, 3.0, -9.0]
y = []

# ------------------------
# write your code here
# ------------------------
def factorise(x):
    return(   3 * x ** 3
            - 2 * x ** 2
            + 3 * x
            - 1
          )           
    
for val in x:
    y.append( factorise(val) )
    
# Validate results
for indx in range(len(x)):
    if expected_res[indx] == y[indx]:
        print(f"When the value in 'x' is {x[indx]} the result of 'y' is {y[indx]}")
    else:
        print(f"Please review the result when 'x' is: {x[indx]}")
        

