#from ecommerce.sales import calc_tax
from ecommerce.shopping import sales
import sys

print(dir(sales))

#print(sys.path)
print("\n sales name ",sales.__name__)
print("\n sales package ",sales.__package__)
print("\n sales file ",sales.__file__)
print("\n sales builtins ",sales.__builtins__)
print("\n sales cached ",sales.__cached__)
print("\n sales loader ",sales.__loader__)

