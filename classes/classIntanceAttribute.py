class Point:
    # class attribute
    default_color = "red"

    def __init__(self,x,y):
        self.x = x
        self.y =y

    def draw(self):
        print(f"Point ({self.x},{self.y})")
Point.default_color = "yellow"
point = Point(2,3)
print("\n Printing class attribute using object",point.default_color)
print("\n Printing class attribute using classname",Point.default_color)
# attributes are dynamic can defined at runtime are instance attributes
point.z = 10
point.draw()

another = Point(3,4)
print("\n Printing class attribute using another object",another.default_color)
another.draw()