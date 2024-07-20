'''
Estimated Time
    10-15 minutes

Difficulty level
    Easy

Objectives
    Improve student skills to define, use, and test functions.
    
Scenario
    The fuel consumption of a car can be expressed in many different ways. For example, in Europe, it is shown as the amount of fuel consumed per 100 kilometers.

    In the USA. In the USA, it is shown as the number of miles traveled by a car with a gallon of fuel.

    Your task is to write a couple of functions that convert l / 100km to mpg (thousands per gallon), and vice versa.

The functions:

    * They are called liters_100km_to_miles_gallon and miles_gallon_to_liters_100km respectively.
    * They take an argument (the value corresponding to their names).
    
    Complement the code in the editor.

    Run your code and check if your output is the same as ours.

    Here is information to help you:

    * 1 mile   = 1609,344 meters.
    * 1 gallon = 3.785411784 liters.
    
Expected departure:

60.31143162393162
31.36194444444444
23.52145833333333
3.9007393587617467
7.490910297239916
10.009131205673757
'''
one_mile   = 1609.344    # meters.
one_gallon = 3.785411784 # liters. 

km_per_mile = 100000 / one_mile
liter_per_galon = 1 / one_gallon

def liters_100km_to_miles_gallon(liters):
    return km_per_mile / (liters * liter_per_galon)


def miles_gallon_to_liters_100km(miles):
    return one_gallon / (miles * (one_mile / 100000))

print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))
