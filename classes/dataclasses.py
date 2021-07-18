from collections import namedtuple
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


#namedtuple("Point")
p1 = Point(1,2)
p2 = Point(1,2)
print("\n address of p1 ",id(p1))
print("\n address of p2 ",id(p2))
print(p1 == p2)

# instead of writing above code for data classes
# can we solved using tuples instead less code
# we do not need to use magic method __eq__ to implemtment equality
Point = namedtuple("PointTuple",["x","y"])
p3 = Point(x=1,y=2)
p4 = Point(x=1,y=2)
print("\n type of p3 ",type(p3))
print("\n are pointed tuple p3 and p4 equal ",p3 == p4)