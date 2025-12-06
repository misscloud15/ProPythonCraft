
class Collage:                #class created
    degree = "btech"            #class attributes
    branch = "AIML"

    def getinfo(self):
        print(f"The Degree of student is{self.degree} and enrolled in Branch {self.branch}")

    @staticmethod
    def greet():
        print("Good Morning")

student = Collage()
student.getinfo()
student.greet()









