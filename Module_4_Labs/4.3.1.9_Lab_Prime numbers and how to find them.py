'''
Estimated Time
    15-20 minutes

Difficulty level
    Means

Objectives
    * Familiarize the student with classic notions and algorithms.
    * Improve student skills to define and employ functions.

Scenario
    A natural number is cousin if it is greater than 1 and has no dividers more than 1 and itself.

    ¿Complicated? No way. For example, 8 is not a prime number, since you can divide it by 2 to 4 (we cannot use divisors equal to 1 and 8, as the definition prohibits it).

    On the other hand, 7 is a prime number, since we cannot find any divisors for it.


    Your task is to write a function that verifies whether a number is prime or not.

Function:

    * Is called is_prime.
    * Take an argument (the value to verify).
    * Returns True if the argument is a prime number, and False otherwise.
    
    Tip: try dividing the argument by all subsequent values (starting from 2) and check the rest: if it is zero, your number cannot be a prime number; carefully analyze when you should stop the process.

    If you need to know the square root of any value, you can use the operator **. Remember: the square root of x it's the same as x0.5.

    Complement the code in the editor.

    Run your code and check if your output is the same as ours.

Test data
    Expected output:

    2 3 5 7 11 13 17 19
'''
def is_prime(num):
    if num % 2 == 0:     #Even
        return False
    else:                #Prime
        return True

for i in range(1, 20):
	if is_prime(i + 1):
			print(i + 1, end=" ")
print()
