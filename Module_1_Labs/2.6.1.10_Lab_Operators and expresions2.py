'''
Estimated Time
    20 minutes

Difficulty level
    Intermediate

Objectives
    * Become familiar with the concepts of numbers, operators, and arithmetic expressions in Python.
    * Understand the precedence and associativity of Python operators, as well as the correct use of parentheses.

Scenario
    The task is to complete the code in order to evaluate the following expression:
    
    <img> url=https://edube.org/uploads/media/default/0001/01/b28be61cd2ada9483ab1e86e8be7b0b797d24674.png />

    The result must be assigned to y. Be cautious, look at the operators and prioritize them. Use as many parentheses as necessary.

    You can use additional variables to shorten the expression (however, it is not very necessary). Test your code carefully.


Test Data
    Sample input: 1
    Expected departure:
        y = 0.6000000000000001

    Sample input: 10
    Expected departure:
        y = 0.09901951266867294

    Sample input: 100
    Expected departure:
        y = 0.009999000199950014

    Sample input: -5
    Expected departure:
        y = -0.19258202567760344
'''


# ------------------------
# code your test data here
# ------------------------
x =  [float(test) for test in [1, 10, 100, -5] ]
expected_res = [0.6000000000000001, 0.09901951266867294, 0.009999000199950014, -0.19258202567760344]
y = []

# ------------------------
# write your code here
# ------------------------
# Make the calculations
def algebraic_expansion(x):
    return(  1 / (x + 1 / (x + 1 / (x + 1 / x))))           

for val in x:
    # y.append( algebraic_expansion(val) )
    y.append( algebraic_expansion(val) )     
    
# Validate results
for indx in range(len(x)):
    if expected_res[indx] == y[indx]:
        print(f"When the value in 'x' is {x[indx]} the result of 'y' is {y[indx]}")
    else:
        print(f"Please review the result when 'x' is: {x[indx]}")
        