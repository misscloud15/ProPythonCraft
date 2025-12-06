class Device:
    def __init__(self):
        print("Device constructor")

    def power_on(self):
        print("Device is powered on.")

class Laptop(Device):
    def __init__(self):
        print("Laptop constructor")

    def boot(self):
        print("Laptop is booting...")

class GamingLaptop(Laptop):
    def __init__(self):
        super().__init__()
        print("GamingLaptop constructor")
    
    def run_game(self):
        print("Running high-end game...")
        
gl = GamingLaptop()
gl.power_on()
gl.boot()
gl.run_game()
