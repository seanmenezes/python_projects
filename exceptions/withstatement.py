try:
    # if object like File has context management protocol that is it
    #  has methods special methods like 
    # __enter and __exit
    # we can use such objects along with clause
    #python will automatically call the the __exit method
    # and there it will release external resources.
    with open("app.py") as file,open("filter.py") as target:
        print("File Opened.")
    age = int(input("Age: "))
    xfactor = 10/age
except (ValueError,ZeroDivisionError):
    print("you didn't enter a valid age.")
else:
    print("No exceptions were thrown.")