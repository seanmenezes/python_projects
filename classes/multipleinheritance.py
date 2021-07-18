# Multiple inheritance is not bad its bad if you do not use it 
# properly
# if two classes have seperate features and you want to inherit both those features
# in a third classs
# problem occurs when two classes you are inheriting share features.
class Flyer: 
    def fly(self):
        pass


class Swimmer:
    def swim(self):
        pass


class FlyingFish(Flyer,Swimmer):
    pass