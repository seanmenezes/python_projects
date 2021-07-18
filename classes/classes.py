class Point:
    def __init__(self,x,y):
        self.x = x
        self.y =y

    def draw(self):
        print(f"Point ({self.x},{self.y})")

point = Point(2,3)
print(type(point))
print("\n Is point instance of Point class ",isinstance(point,Point))
print("\n print value of x ",point.x)
point.draw()