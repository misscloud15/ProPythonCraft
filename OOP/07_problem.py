# . Add a static method in problem 2, to greet the user with hello. 

#. Write a class “Calculator” capable of finding square, cube and square root of a number. 


class Clculator:

    @staticmethod
    def greet():
        print("Welcome to the user!")

    def __init__(self,n):
        self.n = n

    def square(self):
        print(f"The square of given number {self.n} is {self.n * self.n}. ")

    def cube(self):
        print(f"The cube of given number {self.n} is {self.n * self.n * self.n}. ")

    def squareroot(self):
        print(f"The squareroot of given number {self.n} is {self.n ** 1/2}. ")

a = Clculator(4)
a.greet()
a.square()
a.cube()
a.squareroot()

        



