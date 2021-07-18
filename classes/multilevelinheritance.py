# want to ue inheritance limit it to one or max two levels else
#you are shooting yourself in the foot.
class Animal:
    def eat(self):
        print("eat")

class Bird(Animal):
    def fly(self):
        print("fly")

class Chicken(Bird):
    pass

