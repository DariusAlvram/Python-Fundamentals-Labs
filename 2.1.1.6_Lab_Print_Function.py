'''
Estimated Time
    5-10 minutes

Difficulty level
    Very easy

Objectives
    Become familiar with function print() and its formatting capabilities.
    Experiment with the Python code.
    Scenario
    The command print() , Which is one of Python's simplest directives, it simply prints a line of text on the screen.

In your first laboratory:

    Use the function print() to print the line "¡Hola, Mundo!" on the screen.
    Once this is done, use the function print() again, but this time print your name.
    Delete the double quotes and run the code. Observe the Python reaction. ¿What kind of error occurs?
    Then remove the parentheses, put the double quotes back on and run the code again. ¿What kind of error occurs this time?
    Experience as much as you can. Change double quotes to single quotes, use multiple functions print() on the same line and then on different lines. Notice what is happening.
'''
print("Hello, World!")
print("Dario")
#print(Hello, world!)          #<- SyntaxError: invalid character in identifier
#print("Hello World"           #<- SyntaxError: invalid syntax
print('Hello World!')
#print('Hello, World!")        #<- SyntaxError: EOL while scanning string literal
print('Hello, World!''')
print(                  'Hello, World!')
print('Hello, World!'                  )
# PRINT('Hello, World!')       #<- NameError: name 'PRINT' is not defined
# print)"Hello, World!"(         #<- SyntaxError: invalid syntax