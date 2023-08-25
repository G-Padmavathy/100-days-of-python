# Primitive data types are the basic building blocks of data in programming languages.
# some primitive data type

# string
print("123"+"456")
# integer
print(123+567)
# float
print(3.14159)
# Boolean
is_valid = True
is_not_valid = False

# type conversion
num_char = len(input("what's your name?"))
# <class 'int'>
print(type(num_char))
# convert int into str
new_num_char = str(num_char)
print("your name has " + new_num_char + " characters.")

# type function
a = float(123)
print(type(a))
print(70+float("200.5"))
print(str("a")+str("b"))

# Mathematical Operators in python
# addition
print(3+5)
# subtraction
print(5-4)
# Multiplication
print(3*2)
# division
print(6/3)
# exponent(power of the number)
# 4
print(2**2)

# # PEMDAS
# Parentheses ()
# Exponents **
# Multiplication *
# Division /
# Addition +
# Subtraction -

# 7
print(3*3+3/3-3)


# Number Manipulation And F String in python

# 3
print(round(8/3))
# 2.67
print(round(8/3, 2))

# 2
result = 4/2
# 1
result /= 2
print(result)

# 0
score = 0
# 1
score += 1
print(score)

# F-String
print(f"your score is {score}")
# F-String
score = 0
height = 1.8
isWinning = True
print(f"your score is {score}, your height is {height},you are winning is {isWinning}")




