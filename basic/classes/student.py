class Student:
    def __init__(self,name,phy,chem,bio):
        self.__name = name
        self.phy = phy
        self.chem = chem
        self.bio = bio
    
    def totalObtained(self) -> int:
        return (self.phy + self.chem + self.bio)
    
    def percentage(self):
        return (self.totalObtained()/ 300) * 100

    def getName(self):
        return self.__name

    def setName(self,name):
         self.__name = name
    
    def getRollNumber(self):
        return self.__rollnumber

    def setRollNumber(self,rollnumber):
         self.__rollnumber = rollnumber


student1 = Student("Mark",80,90,40)
print("\n Marks Obtianed",student1.totalObtained())
print("\n Percentage Obtianed",student1.percentage())

student1.setName("Alex")
print("Name: ",student1.getName())
student1.setRollNumber("3789")
print("Roll Numer: ",student1.getRollNumber())
    

