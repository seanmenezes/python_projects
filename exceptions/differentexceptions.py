try:
    file = open("app.py")
    age = int(input("Age: "))
    xfactor = 10/age
except (ValueError,ZeroDivisionError):
    print("you didn't enter a valid age.")
else:
    print("No exceptions were thrown.")
finally:
    file.close()