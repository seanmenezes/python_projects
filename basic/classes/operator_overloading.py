"""
Explanation:

In the below code, we have overloaded the built-in method __add__ (line 6) and __sub__ (line 10) that are invoked when the + and the - operators are used.

Whenever two objects of class Com are added using the + operator, the overloaded __add__ method is called.

This method adds the real property separately and the imag property separately and then returns a new Com class object that is initialized by these sums.

Note that __add__ and __sub__ methods have two input parameters. The first one is self, which we know is the reference to the class itself. The second parameter is other. other is a reference to the other objects that are interacting with the class object.

In line 18, obj2 will be considered the other object, the operator will be called on the obj1 object, and the returned object will be stored in obj3.

In line 19, obj2 will be considered the other object, the operator will be called on the obj1 object, and the returned object will be stored in obj4.

Other has Com class attributes and thus, it has the real and imag properties.

Operator	Method
+	__add__ (self, other)
-	__sub__ (self, other)
/	__truediv__ (self, other)
*	__mul__ (self, other)
<	__lt__ (self, other)
>	__gt__ (self, other)
==	__eq__ (self, other)
"""
class Com:
    def __init__(self, real=0, imag=0):
        self.real = real
        self.imag = imag

    def __add__(self, other):  # overloading the `+` operator
        temp = Com(self.real + other.real, self.imag + other.imag)
        return temp

    def __sub__(self, other):  # overloading the `-` operator
        temp = Com(self.real - other.real, self.imag - other.imag)
        return temp


obj1 = Com(3, 7)
obj2 = Com(2, 5)

obj3 = obj1 + obj2
obj4 = obj1 - obj2

print("real of obj3:", obj3.real)
print("imag of obj3:", obj3.imag)
print("real of obj4:", obj4.real)
print("imag of obj4:", obj4.imag)