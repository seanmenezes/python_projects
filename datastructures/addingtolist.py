letters = ["a","b","b","b","c","d","e","f"]

#Adding to a list
letters.append("g")
# at a specific position use insert
letters.insert(0,"-")
print(letters)
print('\n')
#remove 
#remove end of the list
letters.pop()
print(letters)
# remove item at index
letters.pop(0)
letters.remove('b') #remove first occurance of b
print(letters)
# delete for range of items
del letters[1:3]
print(letters)
#remove all objects use clear method 
letters.clear()
print(letters)
print('\n')
letters = ["a","b","c","f","m","l","m","n","m"]
print(letters.index("b"))
# finding index of letter
if "d" in letters:
    print(letters.index("d"))
# number of occurances of a letters
print(letters.count("m"))