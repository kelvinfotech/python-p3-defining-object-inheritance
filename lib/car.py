from vehicle import Vehicle

# vehicle.py

class Car(Vehicle):
    def __init__(self, wheel_size, wheel_number):
        self.wheel_size = wheel_size
        self.wheel_number = wheel_number
    
    def go(self):
        return "vrrrrrrrooom!"
    
    def fill_up_tank(self):
        return "filling up!"
    
    def go(self):
        return "VRRROOOOOOOOOOOOOOOOOOOOOOOM!!!!!"
