'''
Estimated Time
    10-15 minutes

Difficulty level
    Easy

Objectives
    Familiarize the student with:

        * Use instruction continue in the loops.
        * Reflect real life situations in computer code.
        
Scenario
    The sentence continue it is used to omit the current block and advance to the next iteration, without executing the statements within the loop.

    Can be used with both while and for.

    Your task here is very special: You must design a vowel eater! Write a program that uses:

        * A loop for.
        * The concept of conditional execution (if-elif-else).
        * The sentence continue.
        
Your program should:

    * Ask the user to enter a word.
    * Use user_word = user_word.upper() to convert the word entered by the user to capital letters; we will talk about calls chain methods and the upper() very soon, don't worry.
    * Use conditional execution and instruction continue to "eat" the following vowels TO , E , I , O , U of the entered word.
    * Print the letters not consumed on the screen, each one on a separate line.

    Test your program with the data we provide.


Test Data

Sample input: Gregory
Expected departure:
G
R
G
R
Y

Sample input: abstemious
Expected departure:
B
S
T
M
S

Sample input: IOUEA
Expected departure:

'''
# Indicar al usuario que ingrese una palabra
# y asignarlo a la variable user_word.
user_word = str(input("Enter a word: ")).upper()
vocals = ["A", "I", "U", "E", "O"]

for letter in user_word:
    if letter in vocals:
        continue
    else:
        print(letter)
