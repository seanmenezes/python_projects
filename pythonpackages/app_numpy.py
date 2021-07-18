import numpy as np

print(np.__version__)

array = np.array([[1,2,3],[4,5,6]])
print("\n print 2 dimensial array ",array)
print("\n type of array",type(array))
print("\n array shape",array.shape)
 

array_zeros= np.zeros((3,4), dtype=int)
array_ones = np.ones((3,4), dtype=int)
array_fives = np.full((3,4),5, dtype=int)
array_random = np.random.random((3,4))
print("\n array_zeros ",array_zeros)
print("\n array_ones ",array_ones)
print("\n array_fives ",array_fives)
print("\n array_random ",array_random)
print("\n print item at 1st row 1st column [0,0] array_random ",array_random[0,0])
print("\n array_random > 0.2 ",array_random > 0.2)
print("\n boolean indexing new array with values > 0.2 \n array_random[array_random > 0.2] ",array_random[array_random > 0.2])

# cool methods
print("\n np.sum(array_random) ",np.sum(array_random))
print("\n np.floor(array_random) ",np.floor(array_random))
print("\n np.ceil(array_random) ",np.ceil(array_random))
print("\n np.round(array_random) ",np.round(array_random))

# arthmetic operations
first_array = np.array([1,2,3,4])
second_array = np.array([1,2,3,4])
print("\n first + second array",first_array + second_array)
print("\n add number to first_array + 5 => ",first_array + 5)

dimensions_inch = np.array([1,2,3,4])
dimensions_cms = dimensions_inch * 2.54
print(dimensions_cms)

# inches to cms done with comprehension
dimensions_inch = [1,2,3,4]
dimensions_cms = [x * 2.54 for x in dimensions_inch]
print("\n inches to cms using comprehension ",dimensions_cms)
