class Animal:               #Parent class.
    def __init__(self,name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")  

class Other(Animal):        # Child class.
    def speak(self):
        print(f"{self.name} barks!")


a = Animal("Generic animal")
a.speak()

b = Other("Dog")
b.speak()


