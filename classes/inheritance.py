class Animal:
    def __init__(self):
        print("Animal Constructor.")
        self.age = 1

    def eat(self):
        print("eat")

# Animal: Parent,Base
# Mammal: Child, Sub
class Mammal(Animal):
    def __init__(self):
        super().__init__()
        print("Mammal Constructor.")
        self.weight = 240

    def walk(self):
        print("walk")

class Fish(Animal):
    def swim(self):
        print("swim")

m = Mammal()
m.eat()
print("mammal age",m.age)
print("mammal weight",m.weight)
fish = Fish()
print("Fish age",m.age)
fish.eat()
print(isinstance(m,Mammal))
print(isinstance(m,Animal))
print(isinstance(m,object))
print(issubclass(Fish,Animal))