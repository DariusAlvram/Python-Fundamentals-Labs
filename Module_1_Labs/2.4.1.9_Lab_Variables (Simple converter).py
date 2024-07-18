'''
Estimated Time
    10 minutes

Difficulty level
    Easy

Objectives
    * Become familiar with and work with the concept of variables.
    *Perform basic operations and conversions.
    *Experiment with the Python code.
    
Scenario
    Miles and kilometers are units of length or distance.

    Keeping in mind that 1 mile equals approximately to 1.61 kilometers, complements the program in the editor to convert from:

    * Miles to kilometers.
    * Kilometers to miles.
    
    The existing code should not be changed. Write your code in the places indicated with ###. Test your program with the data that has been provided in the source code.


    Pay close attention to what is happening within the function print(). It analyzes how multiple arguments are provided for the function, and how the result is displayed.

    Note that some of the arguments within the function print() are strings (for example "millas son", and others are variables (eg miles).

TIP

    There is one more interesting thing that is happening. ¿Can you see another function within the function print()? It is the function round(). Your job is to round the output of the result to the number of decimals specified in the parenthesis, and return a floating value (within the function round() you can find the variable name, the name, a comma, and the number of decimal places you want to display). This function will be discussed more very soon, do not worry if not everything is very clear. You just want to boost your curiosity.


    After completing the lab, open Sandbox, and experience more. Try writing different converters, for example a USD to EUR converter, a temperature converter, etc. ¡Let your imagination fly! Try to show the results by combining strings and variables. Try to use and experiment with the function round() to round your results to one, two or three decimal places. Check what happens if a digit is not provided when rounding. Remember to try your programs.

    Experiment, draw your own conclusions, and learn. Be curious.


Expected result
    7.38 millas son 11.88 kilómetros
    12.25 kilómetros son 7.61 millas
'''

kilometers = 12.25
miles      = 7.38
                                         # (1 * Km ) = 1.6 * (1 * Miles)
miles_to_kilometers = miles * 1.61       # Km        = (Miles * 1.6) / 1
kilometers_to_miles = kilometers / 1.61  # Miles     = Km / 1.6             

print(miles, "millas son", round(miles_to_kilometers, 2), "kilómetros")
print(kilometers, "kilómetros son", round(kilometers_to_miles, 2), "millas")
