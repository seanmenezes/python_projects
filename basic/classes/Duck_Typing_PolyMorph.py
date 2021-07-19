"""
Dynamic typing:
Duck typing extends the concept of dynamic typing in Python.

Dynamic typing means that we can change the type of an object later in the code.
Now coming back to why it is called Duck typing: So, if a bird speaks like a duck, swims like a duck, and eats like a duck, that bird is a duck.

Similarly, in the above example, the animal object does not matter in the definition of the Sound method as long as it has the associated behavior, Speak(), defined in the object’s class definition. In layman terms, since both the animals, dog and cats, can speak like animals, they both are animals. This is how we have achieved polymorphism without inheritance.

Due to the dynamic nature of Python, duck typing allows the user to use any object that provides the required behavior without the constraint that it has to be a subclass. See the code below for a better understanding of dynamic typing in Python:
"""
class Dog:
    def Speak(self):
        print("Woof woof")


class Cat:
    def Speak(self):
        print("Meow meow")


class AnimalSound:
    def Sound(self, animal):
        animal.Speak()


sound = AnimalSound()
dog = Dog()
cat = Cat()

sound.Sound(dog)
sound.Sound(cat)
