items = [
    ("Product1",10),
     ("Product2",9),
     ("Product3",12),
     ("Product4",11),
     ("Product5",8),
     ("Product6",7),
     ("Product7",13),
     ("Product8",5),
     ("Product9",14)
]

prices = list(map(lambda item:item[1],items))
# python has a concept called list comprehension not present in other languages
# [expression for item in items]
# to get price of each item in tuple 
prices_new = [item[1] for item in items]
print(prices_new)

filtered = list(filter(lambda item:item[1] >=10,items))
print('filtered new')
filtered_new  = [item for item in items if item[1] >= 10]
print(filtered_new)