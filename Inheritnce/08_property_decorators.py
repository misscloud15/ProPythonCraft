class Student:
    def __init__(self, name):
        self._name = name   # using a protected attribute

    @property
    def name(self):
        return self._name   # getter

    @name.setter
    def name(self, value):
        if len(value) < 2:
            raise ValueError("Name should be at least 2 characters long")
        self._name = value   # setter

    @name.deleter
    def name(self):
        print("Deleting name...")
        del self._name


s = Student("new")

print(s.name)     # calls the getter → Megha

s.name = "Diya"   # calls the setter

del s.name        # calls the deleter
