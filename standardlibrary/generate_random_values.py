import random
import string

print(random.random())
print(random.randint(1,10))
print(random.choice([1,2,3,4,5]))
print(random.choices([1,2,3,4,5],k=2))

# generate random password
print("".join(random.choices("abcdefghijklmnop$%!@&*())12223344",k=7)))
print("".join(random.choices(string.ascii_letters + string.digits,k=10)))


# shuffle an array of numbers
numbers = [1,2,3,4,5,6,7,9]
random.shuffle(numbers)
print(numbers)