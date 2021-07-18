# tuple = sequence of objects you cannot modify the object
# instead of square brackets use paranthesis to define a tuple
# USAGE - lets say you are dealing with a sequence of objects 
# and you dont want to accidently modify this sequence of object like a read only list.
point1 = (1,2)
# or
point2 = 1,2
#or
point3 = 1,
# empty tuple
point4 = ()

print(type(point1))
print("point 1",point1)
print("point 2",point2)
print("point 3",point3)
print("point 4",point4)

# concatinating tuples
point = (1,2) + (3,4)
print(" concatinated point ", point)
# multiplication operator to repeat tuple
point_repeat = (1,2) * 3
print(" repeat point tuple", point_repeat)
# convert list to tuple
list_to_tuple = tuple([1,2,3])
print('list to tuple ',list_to_tuple)
# convert string to tuple
string_tuple = tuple("Hello World")
print("string to tuple",string_tuple)
# you can access items like list
point = (1,2,3,4,5,6)
print('Items 0, 1,2 ',point[0:3])
print('item 3',point[3])

# unpack tuple
point = (1,2,3)
x,y,z = point
print("x",x)
print("y",y)
print("z",z)

if 10 in point:
    print("exists")

