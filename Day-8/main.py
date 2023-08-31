"""
Functions
def my_function():
    #Do this
    #Then Do this
    #Finally Do this

my_function()// calling a function with function name and round brackets

"""


# Function
def greet():
    print("Hi")
    print("padmavathy")
    print("how are you?")


greet()

# function with input
"""
Functions
def my_function(something):something=parameter is the name of the data
    #Do this something
    #Then Do this
    #Finally Do this

my_function(123) 123= argument is the actual value of the data// calling a function with function name and round brackets
"""


def greet_with_name(name):
    print(f"Hi {name}")
    print(f"we from start coding."
          f"we are organize a webinar in sunday evening 6.00PM. If you interest {name} please register this link.")
    print(f"If you want now more the webinar click below the link.")


greet_with_name("padmavathy")

# function with more than 1 input
"""
positional argument
def function(a,b,c): a=3,b=2,c=1
    do this with a
    then do this with b
    finally do this with c
function(3,2,1)
"""


def greet_with(name, location):
    print(f"I am {name}")
    print(f"I am from {location}")


greet_with("Maya", "Bangalore")
"""
keyword argument
def function(a,b,c): a=3,b=2,c=1
    do this with a
    then do this with b
    finally do this with c
function(c=3,a=1,b=2)
"""


def greet_with(name, location):
    print(f"I am {name}")
    print(f"I am from {location}")


greet_with(location="Bangalore", name="Maya")