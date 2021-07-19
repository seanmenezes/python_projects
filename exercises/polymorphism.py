class Animal():
    def __init__(self,name = "",sound="") -> None:
        self.name = name
        self.sound = sound
    
    
    def Animal_details(self):
        print("Name ",self.name)
        print("Sound ",self.sound)

class Dog(Animal):
    def __init__(self, name, sound,family) -> None:
        super().__init__(name=name, sound=sound)
        self.family = family 

    def Animal_details(self):
        super().Animal_details()
        print("Family ",self.family)   

class Sheep(Animal):
    def __init__(self, name, sound,color) -> None:
        super().__init__(name=name, sound=sound)
        self.color = color 

    def Animal_details(self):
        super().Animal_details()
        print("color ",self.color)

d = Dog("Pongo", "Woof Woof", "Husky")
d.Animal_details()
print(" ")
s = Sheep("Billy", "Baaa Baaa", "White")
s.Animal_details()