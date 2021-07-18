list1 = [1,2,3]
list2 = [10,20,30]

# combing two lists to a list of tuples like this [(1,10),(2,20),(3,30)]
# takes not just list but even a string
print(list(zip("abc",list1,list2)))