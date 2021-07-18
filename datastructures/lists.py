letters = ["a","b","c"]
matrix = [[0,1],[2,3]]
zeros = [0] * 100
print(zeros)
combined = zeros + letters
print(combined)

# using range 
numbers = list(range(2,20))
print(numbers)
chars = list("Hello World")
print(chars)
print(len(chars))
# items in list
letters[0] = "A"
print(letters[0])
print(letters[-1]) # last item in the list.
print(letters[0:3])
print(letters[:3])
number = list(range(20))
print(numbers)
print(numbers[::2])
print(number[::-1]) # all items on the list in reverse order
#list unpacking
number_list = [1,2,3]
first, second, third = number_list
number_list2 = [1,2,3,4,4,4,4,4,9]

first, *other, last = number_list2
print(first, last)
print(other)
#looping through lists
alpabets = ["a","b","c","d","e","f"]
for letter in alpabets:
    print(letter)
for letter in enumerate(alpabets):
    print(letter[0],letter[1])
print("\n")    
# iterating list bu unpacking tuple of enumeration
for index,letter in enumerate(alpabets):
    print(index, letter)

#    
