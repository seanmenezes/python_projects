# operator that comes in handy when working with data structures
# you can unpack any iterable
numbers = [1,2,3,4,5,7,8,9,11,12,13]
print(*numbers)
values = list(range(5))
values = [*range(5),*"Hello"]
print("\n print list",values)

# combine list using unpack operator
first =[1,2,3]
second = [5,6,7]
combined = [*first,"a",*second,*"Hello"]
print(combined)

# unpack dictionaries 
firstDict = { "x":1,"y":2,"z":3}
secondDict ={ "x":20,"b":30}
combined = {**firstDict,**secondDict,"c":40}
print("\n combined dictionary ",combined)