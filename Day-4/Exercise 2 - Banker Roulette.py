""" You are going to write a program that will select a random name from a list of names.
The person selected will have to pay for everybody's food bill.
"""
# Import the random module here
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(",")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
# num_items = len(names)
# pick_random_name = random.randint(0, num_items-1)
# person_who_will_pay = names[pick_random_name]

person_who_will_pay = random.choice(names)
print(f"{person_who_will_pay} is going to buy the meal today.")
