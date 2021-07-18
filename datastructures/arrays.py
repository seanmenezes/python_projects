# when you have a very list of values use an array
from array import array
# define array - array("type code,list")
numbers = array("i",[1,2,3])
# similar to list you can append etc
numbers.append(4) 
numbers.insert(3,5)

print("\n after append & insert",numbers)
numbers.pop()
print("\n pop",numbers)
# like list we can assign a value to index element however unlike list array 
# objects are typed hence you need to use same type int based on type created at init 
# not float etc
numbers[0] =10;
print("\n after assignent", numbers)