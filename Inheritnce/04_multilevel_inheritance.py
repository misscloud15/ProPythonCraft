class Vehicle:
    def start(self):
        print("This machine is vehicle named car.")
        
class Car(Vehicle):
    def wheels(self):
        print("The car has four wheels. ")
        
class Lucurycar(Car):
    def name(self):
        print("Known as one of luxury cars. ")
        


c = Lucurycar()
c.start()
c.wheels()
c.name()
