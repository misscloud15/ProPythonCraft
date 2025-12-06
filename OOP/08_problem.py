# 5. Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats) 
# and get fare information of train running under Indian Railways. 

from random import randint

class Train:
    def __init__(self,train_no):
        self.train_no = train_no
        print("Welcome to Indian Railways !")
    
    def book(self,fro,to):
        print(f"Book the train {self.train_no} from {fro} to {to}")

    def getsatatus(self,seats):
        print(f"Book the train {self.train_no} with available {seats}")

    def info(self):
        print(f"Is the {randint(1,200)} train running undef Indian Railways.")


    

a = Train(11111)
a.book("Kirloskarwadi","Pune")
a.getsatatus(20)
a.info()



