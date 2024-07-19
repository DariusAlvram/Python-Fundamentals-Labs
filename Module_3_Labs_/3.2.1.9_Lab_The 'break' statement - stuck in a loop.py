'''
Estimated Time
    10 minutes

Difficulty level
    Easy

Objectives
    Familiarize the student with:

        * Use instruction break in the loops.
        * Reflect real life situations in computer code.
Scenario
    Instruction break is implemented to exit / end a loop.

    Design a program that uses a loop while and continually ask the user to enter a word unless you log in "chupacabra" like the secret exit word, in which case the message "¡Has dejado el bucle con éxito". It must be printed on the screen and the loop must end.


    Do not print any of the words entered by the user. Use the concept of conditional execution and sentencing break.
'''
word = str(input('Enter the word "Chupacabra": '))
                
while True:
    if word == "Chupacabra":
        break
    word = str(input('Enter the word "Chupacabra": '))
    
print("¡Has dejado el bucle con éxito")