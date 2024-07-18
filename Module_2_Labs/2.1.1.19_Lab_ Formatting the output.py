'''
Estimated Time
    5-15 minutes

Difficulty level
    Easy

Objectives
    Experiment with existing Python code.
    Discover and fix basic syntax errors.
    Become familiar with function print() and its formatting capabilities.
    Scenario
    We recommend that play with the code that we have written for you and that you make some corrections (perhaps even destructive). Feel free to modify any part of the code, but there is one condition: learn from your mistakes and draw your own conclusions.

Try:

    Minimize the number of function calls print() inserting the sequence \n in the chains.
    Make the arrow twice as big (but keep proportions).
    Duplicate the arrow, placing both arrows side by side; note: a string can be multiplied using the following trick: "cadena" * 2 will "cadenacadena" (We will tell you more about it soon).
    Delete any of the quotes and look closely at Python's answer; pay attention to where Python sees an error: is it the place where the error really exists?
    Do the same with some of the parentheses.
    Change any of the words print in something else (for example from lowercase to uppercase, Print) - What happens now?
    Replace some of the quotes with apostrophes; watch what happens carefully.
'''
print("     *    "*2, 
      "    * *   "*2,
      "   *   *  "*2,
      "  *     * "*2,
      " ***   ***"*2,
      "   *   *  "*2,
      "   *   *  "*2,
      "   *****  "*2, sep="\n" ) 

print(
# Print(                #<- Syntax Error
# ```                   #<- Syntax Error: Invalid syntax
'''
         *
        *  *
       *    *
      *      *
     *        *
    *          *
   *            *
  *              *
 *                *
******        ******
     *        *
     *        *
     *        *
     *        *
     *        *
     *        *
     **********  
''')
