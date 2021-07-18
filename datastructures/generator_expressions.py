from sys import getsizeof

values = [x * 2 for x in range (10)]
for x in values:
    print(x)
# if working with large data set or infinite stream of data
# you should not store all those values in memory
# better to use a generator object, they do not store value in memory 
# but in each iteration generate a new value
# below values is no longer a list but a generator object
# whats interesting is size of generator object
# as generator object does not store all values in memory you won't get total
# number of items you are working with
values = (x * 2 for x in range (10))
print("\n",values)
for x in values:
    print(x)

print("\n generator object size for 1000 values")
values = (x * 2 for x in range (1000))
print("gen for 1000 numbers:",getsizeof(values))

print("\n generator object size for 100000 values")
values = (x * 2 for x in range (100000))
print("gen for 100000 numbers:",getsizeof(values))

print("\n list size for 100000 values")
values = [x * 2 for x in range (100000)]
print("gen for 100000 numbers:",getsizeof(values))