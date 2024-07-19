'''
Estimated Time
    10-15 minutes

Difficulty level
    Easy

Objectives
    Familiarize the student with:

        * Create and modify simple lists.
        * Use methods to modify lists.
    
Scenario
    The Beatles were one of the most popular music groups of the 1960s and the best-selling band in history. Some people consider them the most influential act of the rock era. In fact, they were included in the magazine compilation Time of the 100 most influential people of the 20th century.

    The band underwent many formation changes, culminating in 1962 with the formation of John Lennon, Paul McCartney, George Harrison, and Richard Starkey (better known as Ringo Starr).


    Write a program that reflects these changes and allows you to practice with the list concept. Your task is:

        Step 1: Create an empty list called beatles.
        Step 2: Use the method append() to add the following band members to the list: John Lennon, Paul McCartney and George Harrison.
        Step 3: Use the loopfor and the append() to ask the user to add the following band members to the list: Stu Sutcliffe, and Pete Best.
        Step 4: Use the instruction del to eliminate Stu Sutcliffe and Pete Best from the list.
        Step 5: Use the method insert() to add to Ringo Starr at the top of the list.

    By the way, are you a Beatles fan? (The Beatles are one of Greg's favorite bands. But wait...¿Who's Greg?)
'''
# paso 1
Beatles = []
print("Paso 1:", Beatles)

# paso 2
Beatles.append('John Lennon')
Beatles.append('Paul McCartney')
Beatles.append('George Harrison')
print("Paso 2:", Beatles)

# paso 3
for indx in range(2):
    Beatles.append( str(input("Add Stu Sutcliffe, and Pete Best:")))
print("Paso 3:", Beatles)

# paso 4
del Beatles[3]
print("Paso 4:", Beatles)

# paso 5
Beatles.insert(0,"Ringo Star")
print("Paso 5:", Beatles)


# Testing the lenght of the list
print("Los Fav", len(Beatles))
