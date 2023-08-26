"""" if/else Statement
 the "if-else" statement allows you to execute different blocks of code depending on whether a certain condition is true
  or false.
    Syntax:
    if condition:
        DO THIS
    else:
        DO THIS
"""
# Example 1:
water_level = 50
if water_level > 80:
    print("drain water")
else:
    print("continue")

# Example 2:
print("Welcome to the roller coaster!")
height = int(input("What is your height in cm?"))
if height >= 120:
    print("you can ride the roller coaster!")
else:
    print("Sorry, you have to grow taller before you can ride.")

""""
COMPARISON OPERATORS
1. >  Greater than
2. <  Less than
3. >= Greater than equal to 
4. <= Less than equal to
5. == Equal to
6. != Not to
"""

"""" Nested if/else statement
In Python, nested if-else statements are used when we need to check multiple conditions one after another. 
It allows us to have if-else statements inside another if-else statement.
    Syntax:
    if condition:
        DO THIS
        if condition:
            DO THIS
        else:
            DO THIS
    else:
        DO THIS
"""
# Example
print("Welcome to the roller coaster!")
height = int(input("What is your height in cm?"))
if height >= 120:
    print("you can ride the roller coaster!")
    age = int(input("What is your age? "))
    if age <= 18:
        print("Please Pay ₹7.")
    else:
        print("please Pay ₹12.")
else:
    print("Sorry, you have to grow taller before you can ride.")

"""" if/elif/else statement
The if/elif/else statement is a control flow statement used in programming to execute different blocks of code based on 
certain conditions. 
It allows you to define multiple conditions and specify different actions to be taken for each condition.
    Syntax:
    if condition1:
        DO A
    elif condition2:
        DO B
    else:
        DO THIS
"""
# Example:
print("Welcome to the roller coaster!")
height = int(input("What is your height in cm?"))
if height >= 120:
    print("you can ride the roller coaster!")
    age = int(input("What is your age? "))
    if age > 12:
        print("Please Pay ₹7.")
    elif age <= 18:
        print("Please Pay ₹7.")
    else:
        print("please Pay ₹12.")
else:
    print("Sorry, you have to grow taller before you can ride.")

""" Multiple if statement
    syntax:
    if condition:
        DO A
    if condition:
        DO B
    if condition:
        DO C
"""
# Example:
print("Welcome to the roller coaster!")
height = int(input("What is your height in cm?"))
bill = 0

if height >= 120:
    print("you can ride the roller coaster!")
    age = int(input("What is your age? "))
    if age > 12:
        bill = 5
        print("Please Pay ₹5.")
    elif age <= 18:
        bill = 7
        print("Please Pay ₹7.")
    else:
        bill = 12
        print("please Pay ₹12.")

    wants_photo = input("Do you want a photo taken? Y or N.")
    if wants_photo == "y":
        # bill = bill+3
        bill += 3
    print(f"Your final bill is {bill}.")

else:
    print("Sorry, you have to grow taller before you can ride.")


"""" Logical Operator
    A and B [ture= true =true][false=false=false][true=false=false]
    C or D opposite and operator 
    not E   reverse
"""
# a = 12
# a > 10 and a < 13 = true
# not a > 15

# Example:
print("Welcome to the roller coaster!")
height = int(input("What is your height in cm?"))
bill = 0

if height >= 120:
    print("you can ride the roller coaster!")
    age = int(input("What is your age? "))
    if age > 12:
        bill = 5
        print("Please Pay ₹5.")
    elif age <= 18:
        bill = 7
        print("Please Pay ₹7.")
    # 45 <= age <= 55
    elif age >= 45 and age <= 55:
        print("Everything is going to be ok.Have a free ride on us! ")
    else:
        bill = 12
        print("please Pay ₹12.")

    wants_photo = input("Do you want a photo taken? Y or N.")
    if wants_photo == "y":
        # bill = bill+3
        bill += 3
    print(f"Your final bill is {bill}.")

else:
    print("Sorry, you have to grow taller before you can ride.")







