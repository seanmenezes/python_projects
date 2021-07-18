items = [
    ("Product1",10),
     ("Product2",9),
     ("Product3",12),
     ("Product4",11),
     ("Product5",8),
     ("Product6",7),
     ("Product7",13),
     ("Product8",5),
     ("Product9",14)
]
# lets say you want to filter items over 10 dollars
#two ways to do it
# use build in filter fucntion 
# filter(function or none, iterable) --> filter return iterable of criteria matched
filtered =list(filter(lambda item:item[1] > 10,items))
print(filtered)

