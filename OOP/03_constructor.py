class Collage:                #class created
    degree = "btech"            #class attributes
    branch = "AIML"

    def __init__(self,degree):
        self.degree = degree
        print("I am creating an object !")

    def getinfo(self):
        print(f"The Degree of student is {self.degree} and enrolled in Branch {self.branch}")

    @staticmethod
    def greet():
        print("Welcome !")

student = Collage("BTech")
student.getinfo()
student.greet()