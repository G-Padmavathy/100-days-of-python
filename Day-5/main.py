"""
Loops
For Loop
A for loop is used for iterating over a sequence
(that is either a list, a tuple, a dictionary, a set, or a string).
syntax:
for item in list_of_item:
    do something to each
"""
fruits = ["apple", "banana", "grapes", "peach"]
for item in fruits:
    print(item)
    print(item + "orange")
    print(fruits)

""" Range function"""
# for loop with range
for number in range(1, 11):
    print(number)

for number in range(1, 11, 3):
     print(number)

total = 0
for item in range(1, 101):
    total += item
    print(total)