sentence = "This is a common interview question"
values = [*sentence]
valueMap ={}
for x in values:
    if not valueMap.get(x):
        valueMap[x] = 1
    else:
       valueMap[x] = valueMap.get(x) + 1
maxValue =0
maxKey = ""
for key,value in valueMap.items():
    print(key,value)
    if value > maxValue:
        maxValue = value
        maxKey = key
print("character ",maxKey," value ",maxValue)

        



