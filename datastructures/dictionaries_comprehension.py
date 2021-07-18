values = []
for x in range(5):
    values.append(x * 2)

# comprehension [expression for item in items]
values = [x * 2 for x in range(5)]
print('\n comprehension list',values)

values = {x * 2 for x in range(5)}
print('\n comprehension set',values)

# use comprehension for dictionary
values = {x:x * 2 for x in range(5)}
print('\n comprehension dictionary',values)

# instead of
values = {}
for x in range(5):
    values[x] = x * 2