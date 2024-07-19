'''
Estimated Time
    5 minutes

Difficulty level
    Very easy

Objectives
    Familiarize the student with:

        * Use the loop for.
        * Reflect real life situations in computer code.
Scenario
    ¿Do you know what Mississippi is? Well, it is the name of one of the states and rivers in the United States. The Mississippi River is approximately 2,340 miles long, making it the second longest river in the United States (the longest being the Missouri River). ¡It is so long that a single drop of water takes 90 days to cover its entire length!

    The word Mississippi also used for a slightly different purpose: for count mississippily (mississippimente).

    If you are not familiar with the phrase, we are here to explain what it means: it is used to count seconds.

    The idea behind this is to add the word Mississippi a number counting the seconds out loud makes it sound closer to the clock, and therefore "one Mississippi, two Mississippi, three Mississippi" it will take approximately three real seconds of time. Children who play hide and seek often use it to make sure the seeker counts honestly.


    Your task is very simple here: write a program that uses a loop for to "count mississippi" up to five. Having counted to five, the program should print the final message on the screen "¡Listos o no, ahí voy!"

    Use the skeleton that we have provided in the editor.

EXTRA INFO

    Please note that the code in the editor contains two elements that may not be entirely clear at this time: the statement import time and the method sleep(). We will talk about them soon.

    At the moment, we would like you to know that we have imported the module time and we have used the method sleep() to suspend the execution of each subsequent function of print() inside the loop for for a second, so that the message sent to the console looks like a real count. Don't worry, you will soon learn more about modules and methods.

Expected output
    1 Mississippi
    2 Mississippi
    3 Mississippi
    4 Mississippi
    5 Mississippi
'''
import time

    # Escribe un bucle for que cuente hasta cinco.
    # Cuerpo del bucle: imprime el número de iteración del bucle y la palabra "Mississippi".
    # Cuerpo del bucle - usar: time.sleep (1)
for count in range(1,6):
    print(f"{count} Mississipy")
    time.sleep(1)

# Escribe una función de impresión con el mensaje final.
print("¡Listos o no, ahí voy!")