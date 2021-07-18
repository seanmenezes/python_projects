class Text(str):
    def duplicate(self):
        return self + " " + self

text = Text("Python")
print("\n convert to lower case", text.lower())
print("\n Duplicate it",text.duplicate())

class TrackableList(list):
    def append(self, object):
        print("Append called")
        super().append(object)

list = TrackableList()
list.append("1")
