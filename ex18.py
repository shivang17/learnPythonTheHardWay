# this one is like the scripts with argv

def print_two(*args):
    arg1,arg2 = args
    print(f"arg1 : {arg1}, arg2: {arg2}")

# *args is not recommended, instead we can use the following method.

def print_two_again(arg1,arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

# One argument function

def print_one(arg1):
    print(f"arg1: {arg1}")


# This one takes no arguments

def print_none():
    print("I got nothing")


print_two("Zed","Shaw")
print_two_again("Zed","Shaw")
print_one("First!")
print_none()