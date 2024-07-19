'''
Estimated Time
    10-15 minutes

Difficulty level
    Easy

Objectives
    Familiarize the student with:

        * Indexing lists.
        * Use operatorsin and not in.
        
Scenario
    Imagine a list: not too long or too complicated, just a simple list containing some integers. Some of these numbers may be repeated, and this is the key. We don't want any repetition. We want them to be removed.

    Your task is to write a program that removes all number repeats from the list. The goal is to have a list in which all the numbers appear no more than once.

    Note: Assume that the original list is already inside the code, you do not have to enter it from the keyboard. Of course, you can improve the code and add a part that can carry out a conversation with the user and get all the data.

    Tip: We recommend that you create a new list as a temporary work area, you do not need to update the current list.

    We have not provided test data as it would be too easy. You can use our skeleton instead.
'''
my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
#
# Write your code here
#
aux_list = []

for num in my_list:
    if num not in aux_list:
        aux_list.append(num)
        
my_list = aux_list

print("La lista con elementos únicos:")
print(my_list)
