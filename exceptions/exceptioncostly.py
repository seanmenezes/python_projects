from timeit import timeit

code1 = """
def calculate_xfactor(age):
    if age <=0:
        raise ValueError("Age cannot be zero or less.")
    return 10/age
try:
    calculate_xfactor(-1)
except ValueError as error:
    pass
"""


code2 = """
def calculate_xfactor(age):
    if age <=0:
        return None
    return 10/age

xfactor =calculate_xfactor(-1)

if xfactor == None:
     pass
"""
# below code will run code 1000 times and give time
# as a general rule when you want to raise an exception think twice
# see if you can solve it with simple if statement
# specially for programs that are used or called many times.
# Raise exceptions only if you really have to.
print("first code",timeit(code1, number=10000))
print("second code",timeit(code2, number=10000))