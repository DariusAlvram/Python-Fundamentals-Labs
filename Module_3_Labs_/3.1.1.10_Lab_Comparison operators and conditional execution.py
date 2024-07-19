'''
Estimated Time
    5-10 minutes

Difficulty level
    Easy

Objectives
    * Become familiar with function input ().
    * Become familiar with comparison operators in Python.
    * Become familiar with the concept of conditional execution.

Scenario
    Spatifil, More commonly known as the crib plant of Moses or flower of peace, it is one of the most popular indoor plants that filters harmful toxins from the air. Some of the toxins it neutralizes include benzene, formaldehyde, and ammonia.

    Imagine that your computer program loves these plants. Every time you receive an entry in the form of the word Espatifilo, involuntarily yells at the console the following string: "¡Espatifilo es la mejor planta de todas!"


    Write a program that uses the concept of conditional execution, take a string as input, and:

        * Print the statement "Si, ¡El ESPATIFILIO! es la mejor planta de todos los tiempos!" on the screen if the entered string is "ESPATIFILIO".
        * Print "No, ¡quiero un gran ESPATIFILIO!" if the entered string is "espatifilo".
        * Print "¡ESPATIFILIO!, ¡No [entrada]!" otherwise. Note: [entrada] is the string that is taken as input.

    Test your code with the data we provide you. ¡And get a SPATIFILY too!


Test Data
    Sample input: espatifilo
    Expected result: No, ¡quiero un gran ESPATIFILIO!

    Example input: pelargonio
    Expected result: !ESPATIFILIO!, ¡No pelargonio!

    Sample input: ESPATIFILIO
    Expected result: Si, ¡El ESPATIFILIO es la mejor planta de todos los tiempos!
'''
plant = str(input("Enter the cientific name of plant of moses: "))

if plant == "ESPATIFILIO":
    answer = "Si, ¡El ESPATIFILIO! es la mejor planta de todos los tiempos!"
elif plant == "espatifilio":
    answer = "No, ¡quiero un gran ESPATIFILIO!"
else:
    answer = f"¡ESPATIFILIO!, ¡No {plant}!"

print(answer)