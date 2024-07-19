'''Estimated Time
10-15 minutes

Difficulty level
Easy / Medium

Objectives
    Familiarize the student with:

    * Use the sentence if-else to branch the control route.
    * Build a complete program that solves simple real-life problems.
Scenario
    Once upon a time there was a land of milk and honey, inhabited by happy and prosperous people. People paid taxes, of course, their happiness had limits. The most important tax, called Personal Income Tax (IPI, for short) had to be paid once a year and was evaluated using the following rule:

        * If the citizen's income did not exceed 85,528 pesos, the tax was equal to 18% of the income minus 556 pesos and 2 cents (this was the call tax exemption ).
        * If the income was higher than this amount, the tax was equal to 14,839 pesos and 2 cents, plus 32% of the surplus over 85,528 pesos.

    Your task is to write a tax calculator.

        * You must accept a floating point value: income.
        * Next, you must print the calculated tax, rounded to total pesos. There is a function called round() who will round for you, you will find it in the skeleton code of the editor.
        * Note: This happy country never returns money to its citizens. If the calculated tax is less than zero, it only means that there is no tax (the tax equals zero). Keep this in mind during your calculations.

    Look at the code in the editor: just read an input value and generate a result, so you need to complete it with some smart calculations.

    Test your code with the data we have provided.

Test Data
Sample input: 10000
Expected result: El impuesto es: 1244.0 pesos

Sample input: 100000
Expected result: El impuesto es: 19470.0 pesos

Sample input: 1000
Expected result: El impuesto es: 0.0 pesos

Sample input: -100
Expected result: El impuesto es: 0.0 pesos
'''
income= int(input("Enter your annual income: "))
Threshhold = 85828


if income <= Threshhold:
    tax  = income * .18 - 556.02
else:
    tax = 1439 + ( .32 * ( income - Threshhold))
    
if tax < 0:
    tax = 0.0 

tax = round(tax, 0)
print("The budget is: ", tax, "pesos")