# dictionary key value pair
# only immutable types can be used as keys, values can be of any type
point = {"x":1,"y":2}
newDict = dict(usa='sean',indo='regina',china='nasya')
print("\n dict",newDict)
newDict["china"] = 'damian'
print("\n dict",newDict)
newDict["japan"] = 'yuki'
print("\n dict after adding",newDict)

if "uae" in newDict:
    print(newDict["uae"])

# another way use get method that return none if key does not exist
print("\n try getting non-existent key using get --> ",newDict.get("uae"))
# another way use get method that return default vlaue if key does not exist
print("\n try getting non-existent key using get default value --> ",
newDict.get("uae",0))

newDict["uae"] = 'muazzam'
# delete item
del newDict["japan"]

print("\n dict after delete",newDict)
print("\n iterating dictionary")
# way 1 iterating through dictionary
for key in newDict:
    print(key, newDict[key])
print("\n way2 using tuple ")   
# way 2 getting a tuple
for tupleValue in newDict.items():
    print(tupleValue)

print("\n way3 using tuple unpack ")   
# way 2 getting a tuple
for key,value in newDict.items():
    print(key,value)

