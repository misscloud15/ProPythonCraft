class Programmer:                       #class created
    company = " Microsoft "            #class attribute

    def __init__(self,name,salary,pin):   #function
        self.name = name
        self.salary = salary
        self.pin = pin
        
one = Programmer(" Megha\n",3000000,"\n m001")
print(one.name,one.salary,one.pin,one.company)