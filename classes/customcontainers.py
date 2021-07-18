# implemting your own contianers are useful when you want to add addtional logic 
# to existing implementations like additional fuctionality
class TagCloud:
    # puting __ makes method or class private but its still accessible
    # its more a convention to users not to access it.
    def __init__(self):
        self.__tags = {}
    
    def add(self,tag):
        self.__tags[tag.lower()] = self.__tags.get(tag.lower(),0) +1

    def __getitem__(self,tag):
         return self.__tags.get(tag.lower(),0) 
    
    def __setitem__(self,tag,count):
          self.__tags[tag.lower()] = count

    def __len__(self):
        return  len(self.__tags)  

    def __iter__(self):
        return iter(self.__tags)       

cloud = TagCloud()  
cloud.add("Python")
cloud.add("python")
cloud.add("python")
cloud.add("Java")
cloud.add("java")


print(cloud["python"]) 
cloud["java"] = 10
print("\n Java count",cloud["java"]) 
print(" length of TagCloud", len(cloud))

for key in cloud:
    print(key,cloud[key])
# accessing private members
print(cloud.__dict__)
print("Accessing private members ",cloud._TagCloud__tags)   

  