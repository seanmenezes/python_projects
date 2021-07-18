items = [
    ("Product1",10),
     ("Product2",9),
     ("Product3",12),
]

prices = []
for item in items:
    prices.append(item[1])
    
print(prices)
# better or more elegant way
# map(func, *iterables)
# first item lambda function, second item list of iterables
# return x a map object which is another iterable
print('using map object to extract price')
x = map(lambda item: item[1], items)
for item in x:
    print(item)
print('after converting map to list')
# other option convert map object to list object
y = list(map(lambda item: item[1], items))
print(y)
