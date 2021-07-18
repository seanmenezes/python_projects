numbers = [3,51,2,8,6]
# sort works on existing list 
numbers.sort()
print(numbers)
numbers.sort(reverse=True)
print(numbers)
#sorted returns new list
print(sorted(numbers))
numbers.sort()
print(sorted(numbers,reverse=True))

print('\n')
# sorting list of tuples
items = [
    ("Product1",10),
     ("Product2",9),
     ("Product3",12),
]

def sort_item(item):
    return item[1]

items.sort(key=sort_item)
print(items)

# rewriting above code using lambda
# key=lambda parameter: return expression
items.sort(key=lambda item:item[0])
print(items)
