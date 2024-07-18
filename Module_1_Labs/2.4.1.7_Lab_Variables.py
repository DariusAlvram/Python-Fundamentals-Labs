'''
Estimated Time
    10 minutes

Difficulty level
    Easy

Objectives
    Become familiar with the concept of storing and working with different types of data in Python.
    Experiment with the code in Python.
Scenario
    Here is a story:

    Once upon a time in the Apple Land, John had three apples, Mary had five apples, and Adam had six apples. They were all very happy and lived for a very long time. End of story.

    Your task is:

    * Create the variables: juan, maria, and adan.
    * Assign values to variables. The value must be equal to the number of apples that each one had.
    * Once the numbers have been stored in the variables, print the variables on one line, and separate each one with a comma.
    * Then you must create a new variable called total_manzanas and must be equal to the sum of the three previous variables.
    * Print the value stored in total_manzanas on the console.
    * Experiment with your code: creates new variables, assigns different values to them, and performs various arithmetic operations with them (for example, +, -, *, /, //, etc.). Try putting a string with an integer together on the same line, for example, "Número Total de Manzanas:" and total_manzanas.
'''

#-> Variables
juan  = 3
maria = 5
adan  = 6

#-> Print Variables
print(f"Juan  = {juan}\nMaria = {maria}\nAdan  = {adan}")

# Sum total apples
total_apples =  (juan  +
                 maria +
                 adan  )

print(f"Total number of apples: {total_apples}")

#-> Experiment with the code using other math operations
num_persons = 3
print(f"Apples per person from total: {total_apples/num_persons}")
print(f"Apples per person from total (truncated): {total_apples//num_persons}")
print(f"Total of apples: {(total_apples/num_persons)*num_persons}")
print(f"Total of apples (Juan + Adan): {total_apples-maria}")