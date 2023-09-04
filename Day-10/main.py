"""
Day-10 function with outputs
"""


def format_name(first_name, last_name):
    if first_name == "" or last_name == "":
        return "please enter your fristname and last name"
    print(f"{first_name} {last_name}")
    return f" Result: Hi {first_name} {last_name}"



f_name = input("Enter your firstname:").title()
l_name = input("enter your lastname:").title()

format_name(f_name, l_name)