# collection with no duplicates defined by curly braces
# not ordered or indexed hence you cannot access an item by index
numbers = [1,1,2,3,3,3,4,5,5,5,5,5]
uniques = set(numbers)
print("set converted",uniques)
newSet = { 4,5,6,7,8,9,9,10,12,15,19,21}
print("\n newSet",newSet)
newSet.add(22)
print("\n after adding",newSet)
newSet.remove(22)
print("\n after adding",newSet)
print("\n set length",len(newSet))

print("\n union set",uniques | newSet)
print("\n intersection set",uniques & newSet)
print("\n difference set",uniques -  newSet)
# semantic difference items in first and second set but not in both
print("\n semantic difference set",uniques ^ newSet)

if 1 in numbers:
    print("\n yes")