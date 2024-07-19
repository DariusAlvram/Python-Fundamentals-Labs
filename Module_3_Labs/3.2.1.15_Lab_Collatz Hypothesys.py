'''
Estimated Time
    20 minutes

Difficulty level
    Average

Objectives
    Familiarize the student with:

        *Use the loop while.
        *Convert verbally defined loops to real Python code.
        
Scenario
    In 1937, a German mathematician named Lothar Collatz formulated an intriguing hypothesis (not yet proven) that can be described as follows:

        1. Take any non-negative and non-zero integer and name it c0.
        2. If it is even, evaluate a new c0 as c0 Ã· 2.
        3. Otherwise, if it is odd, evaluate a new  c0  as 3 Ã c0 + 1.
        4. Yes c0 â  1, jump to point 2.
    The hypothesis says that regardless of the initial value of c0, the value always tends to 1.

    Of course, it is an extremely complex task to use a computer to test the hypothesis of any natural number (it may even require artificial intelligence), but you can use Python to verify some individual numbers. Maybe you even find the one that would refute the hypothesis.

    Write a program that reads a natural number and executes the previous steps whenever c0 be different from 1. We also want you to count the steps necessary to achieve the goal. Your code must also show all the intermediate values of c0.

Tip: The most important part of the problem is how to transform the idea of Collatz into a loop while- this is the key to success.

    Test your code with the data we have provided.

Test Data

    Sample input: 15
        Expected departure:
            46
            23
            70
            35
            106
            53
            160
            80
            40
            20
            10
            5
            16
            8
            4
            2
            1
        pasos = 17

    Sample input: 16
        Expected departure:
            8
            4
            2
            1
        pasos = 4
'''
c0 = int(input("Enter any number (No negatives or zero): "))
steps = 0

# If is even, evaluates again (C0 % 2)
while c0 != 1:
    if c0 % 2 == 0:     #Even
        c0 = c0 // 2
    else:
        c0 = c0 *3 + 1  #Odd
    
    steps += 1          #Increase the number of steps (interations)
    
    print(c0)
    
print(f"Steps = {steps}")