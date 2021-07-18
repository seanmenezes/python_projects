class Rectangle:
    def __init__(self,length=0,width=0):
        self.__length = length
        self.__width = width

    def area(self):
        return (self.__length * self.__width)

    def perimeter(self):
        return 2 * (self.__length + self.__width)

rectangle1 = Rectangle(4,5)
print("\n Rectangle Area => ",rectangle1.area())
print("\n Rectangle Perimeter => ",rectangle1.perimeter())
