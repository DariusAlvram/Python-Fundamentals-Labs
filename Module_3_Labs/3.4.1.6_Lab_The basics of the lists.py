'''
Estimated Time
    5 minutes

Difficulty level
    Very easy

Objectives
    Familiarize the student with:

        * Use basic instructions related to lists.
        * Create and modify lists.
        
Scenario
    Once upon a time there was a hat. The hat did not contain a rabbit, but a list of five numbers: 1, 2, 3, 4 and 5.

Your task is:

    * Write a line of code that asks the user to replace the center number in the list with an integer entered by the user (Step 1).
    * Write a line of code that removes the last item from the list (Step 2).
    * Write a line of code that prints the length of the existing list (Step 3).

¿Ready for this challenge?
'''
hat_list = [1, 2, 3, 4, 5]  # Esta es una lista existente de números ocultos en el sombrero.

# Paso 1: escribe una línea de código que solicite al usuario
# reemplazar el número de en medio con un número entero ingresado por el usuario.
print(hat_list)
hat_list[2] = int(input("Update a new value to the middle item (3): "))

# Paso 2: escribe aquí una línea de código que elimine el último elemento de la lista.
del hat_list[-1]

# Paso 3: escribe aquí una línea de código que imprima la longitud de la lista existente.
print(f"The number of items in this list is: {len(hat_list)}")
print(hat_list)
