'''
Estimated Time
    20-30 minutes

Difficulty level
    Means

Objectives
    Familiarize the student with:

        * Use the loop while.
        * Find the proper implementation of verbally defined rules.
        * Reflect real life situations in computer code.
        
Scenario
    Listen to this story: A boy and his father, a computer programmer, play with wooden blocks. They are building a pyramid.

    Its pyramid is a bit rare, since it is actually a pyramid-shaped wall, it is flat. The pyramid is stacked according to a simple principle: each bottom layer contains one block more than the top layer.

    The figure illustrates the rule used by builders:

    <img src=https://edube.org/uploads/media/default/0001/02/PE1_source_file_ESP_3.2.1.14_ESP.png/>

    Your task is to write a program that reads the number of blocks that builders have, and generate the height of the pyramid that can be built using these blocks.

    Note: Height is measured by the number of complete layers: If builders don't have enough blocks and can't complete the next layer, they finish their job immediately.

    Test your code with the data we have provided.


Test Data
    Sample input: 6
    Expected departure: La altura de la pirámide es: 3

    Sample input: 20
    Expected departure: La altura de la pirámide es: 5

    Sample input: 1000
    Expected departure: La altura de la pirámide es: 44

    Sample input: 2
    Expected departure: La altura de la pirámide es: 1
'''
blocks = int(input("Enter the number of blocks: "))

#Starting from the top of the pyramid (This one contais only one cube)
layer  = 1
height = 0

while blocks >= layer:
    blocks -= layer   #Removes the block in the current layer
    
    height += 1       #Augment the height counter
    layer  += 1       #Set the next layer to ve reviewed
    
print(f"The height of the pyramid is: {height}")