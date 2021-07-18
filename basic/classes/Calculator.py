class Calculator:
    def __init__(self,num1,num2) -> None:
        self.num1 = num1
        self.num2 = num2
    
    def add(self):
        return (self.num2 + self.num1)
    
    def subtract(self):
        return (self.num2 - self.num1)
    
    def multiply(self):
        return (self.num2 * self.num1)
    
    def divide(self):
        return (self.num2 / self.num1)

calculator1 = Calculator(2,4)
print("\n calculator1.add() => ",calculator1.add())
print("\n calculator1.subtract() => ",calculator1.subtract())
print("\n calculator1.multiply() => ",calculator1.multiply())
print("\n calculator1.divide() => ",calculator1.divide())

calculator2 = Calculator(2.0,4.0)
print("\n calculator1.add() => ",calculator2.add())
print("\n calculator1.subtract() => ",calculator2.subtract())
print("\n calculator1.multiply() => ",calculator2.multiply())
print("\n calculator1.divide() => ",calculator2.divide())
