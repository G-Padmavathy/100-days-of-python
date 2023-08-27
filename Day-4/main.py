# DAY-4 Randomisation and Python List

# print random number
# Module:file containing
# import random module
import random
import module
random_integer = random.randint(1, 10)
print(random_integer)
print(module.pi)
# random()-function
random_float = random.random()
round_num = round(random_float*5)
print(round_num)

# List
""""
List are used to store multiple items in a single variable .
List are within [square brackets]
List are ordered, mutable,allow duplicates
Example:
Fruits = ["apple","mango","cherry","strawberry"]
"""
# ordered and positive index value starting from 0
# negative index value start from -1
# allow duplicates apple ,apple
Fruits = ["apple", "apple", "mango", "cherry", "strawberry"]
print(Fruits[1])
print(Fruits[-2])

# mutable means changeable
# change_value_in_list
# ['apple', 'banana', 'cherry', 'strawberry']
Fruits[1] = "banana"
print(Fruits)

# add value to list
# ['apple', 'banana', 'mango', 'cherry', 'strawberry', 'orange']
Fruits.append("orange")
print(Fruits)

# ['apple', 'banana', 'mango', 'cherry', 'strawberry', 'orange', 'orange', 'grapes', 'kiwi']
Fruits.extend(["grapes", "kiwi"])
print(Fruits)

# ['banana', 'mango', 'cherry', 'strawberry', 'orange', 'grapes', 'kiwi']
Fruits.remove("apple")
print(Fruits)

# IndexError

districts_of_tamilnadu = [
    "Ariyalur", "Chennai", "Coimbatore", "Cuddalore", "Dharmapuri", "Dindigul",
    "Erode", "Kanchipuram", "Kanyakumari", "Karur", "Krishnagiri", "Madurai",
    "Nagapattinam", "Namakkal", "Nilgiris", "Perambalur", "Pudukkottai",
    "Ramanathapuram", "Salem", "Sivaganga", "Thanjavur", "Theni", "Thoothukudi",
    "Tiruchirappalli", "Tirunelveli", "Tiruppur", "Tiruvallur", "Tiruvannamalai",
    "Tiruvarur", "Vellore", "Viluppuram", "Virudhunagar", "Tenkasi", "Ranipet",
    "Chengalpattu", "Kallakurichi", "Tirupattur", "Mayiladuthurai"
]

# print(districts_of_tamilnadu[38]) it will raise an error [list index out of range]
num_of_state = len(districts_of_tamilnadu)
print(districts_of_tamilnadu[num_of_state - 1])

""" Working with nested list
 list within in a list is called nested list 
 [['Strawberries', 'Nectarines', 'Apples', 'Grapes', 'Peaches', 'Cherries', 'Pears'],
  ['Spanish', 'Kale', 'Tomatoes', 'Celery', 'Potatoes']]

 """
# example

# dirty_dozen = ["Strawberries", "Spanish", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears",
#                "Tomatoes", "Celery", "Potatoes"]

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spanish", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]
print(dirty_dozen)