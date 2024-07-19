'''
Estimated Time
    5-10 minutes

Difficulty level
    Easy

Objectives
    Familiarize the student with:

        * Use instruction continue in the loops.
        * Modify and update the existing code.
        * Reflect real life situations in computer code.
        
Scenario
    Your task here is even more special than before: You must redesign the vowel eater (ugly) from the previous lab (3.1.2.10) and create a better improved vowel eater! Write a program that uses:

        * A loop for.
        * The concept of conditional execution (if-elif-else).
        * Instruction continue.
        
Your program should:

        * Ask the user to enter a word.
        * Use user_word = user_word.upper() to convert the word entered by the user to capital letters; we will talk about calls chain methods and the upper() very soon, don't worry.
        * Employs conditional execution and instruction continue to "eat" the following vowels TO , E , I , O , U of the entered word.
        * Assign unused letters to variable word_without_vowels and print the variable on the screen.
    Analyze the code in the editor. We have created word_without_vowels and we have assigned you an empty string. Use the concatenation operation to ask Python to combine the selected letters into a longer string during the next loop spins, and assign it to the variable word_without_vowels.

    Test your program with the data we provide.

Test Data
    Sample input: Gregory
    Expected departure:

    GRGRY
    Sample input: abstemious
    Expected departure:

    BSTMS
    Sample input: IOUEA
    Expected departure:
'''
word_without_vowels = ""

# Indicar al usuario que ingrese una palabra
# y asignarla a la variable user_word.
user_word = str(input("Enter a word: ")).upper()

for letter in user_word:
    if letter   == "A":
        continue
    elif letter == "E":
        continue
    elif letter == "I":
        continue
    elif letter == "O":
        continue
    elif letter == "U":
        continue
    else:
        word_without_vowels += letter
   # Completa el cuerpo del bucle.

# Imprimir la palabra asignada a word_without_vowels.
print(word_without_vowels)