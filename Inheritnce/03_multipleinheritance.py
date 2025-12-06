class Employee:
    def company(self,com):
        self.com = com
        print(f"The employee works in {self.com} ")

    def department(self,name):
        print(f"and works in {name} department")

class Prolanguage:
    language = "python"
    def prolang(self):
        print(f"The language that used here is {self.language}.")

class Person(Employee,Prolanguage):
    def name(self,na,id,role):
        print(f"Name:{na}")
        print(f"ID:{id}")
        print(f"Role:{role}")

    

# a = Employee()
# a.company("Microsoft")
# a.department("developer")

b = Person()
b.company("Microsoft")
b.department("web_development")
b.name("Shanti","moo1","coder")
b.prolang()
