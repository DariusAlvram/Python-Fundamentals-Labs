'''
Estimated Time
    15 minutes

Difficulty level
    Easy

Objectives
    Familiarize the student with:

        * Use the loop while.
        * Reflect real life situations in computer code.

Scenario
    A junior magician has chosen a secret number. You have hidden it in a variable called secret_number. He wants everyone who runs his show to play the game Guess the secret number, And guess what number you have chosen for them. ¡Who does not guess the number will be caught in an endless loop forever! Unfortunately, he does not know how to complete the code.

    Your task is to help the magician complete the code in the editor in such a way that the code:

        * It will ask the user to enter an integer.
        * Will use a loop while.
        * It will check if the number entered by the user is the same as the number chosen by the magician. If the number chosen by the user is different from the secret number of the magician, the user should see the message "¡Ja, ja! ¡Estás atrapado en mi bucle!"  and you will be asked to enter a number again. If the number entered by the user matches the number chosen by the magician, the number must be printed on the screen, and the magician must say the following words: "¡Bien hecho, muggle! Eres libre ahora".
        
    ¡The magician is counting on you! Don't disappoint him.


EXTRA INFO
    By the way, look at the function print(). The way we have used it here is called multiline printing. Can use triple quotes to print strings on multiple lines to make it easier to read the text or create a special text-based design. Experiment with it.
'''
secret_number = 777

print(
"""
+==================================+
| ¡Bienvenido a mi juego, muggle!  |
| Introduce un número entero       |
| y adivina qué número he          |
| elegido para ti.                 |
| Entonces,                        |
| ¿Cuál es el número secreto?      |
+==================================+
""")

guessed_num = int(input())

while guessed_num != secret_number:
    print("¡Ja, ja! ¡Estás atrapado en mi bucle!")
    guessed_num = int(input("Intentalo nuevamente ¿Cúal es el número secreto?"))

print("¡Bien hecho, muggle! Eres libre ahora")