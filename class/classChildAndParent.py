"""
Example about Cars based on Child and Parent Class
"""
class car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.km_reading = 0
    def getDes(self):
        long_name = str(self.year)+' '+self.make+' '+self.model
        return long_name.title()

    def read_km(self):
        print("this car has "+ str(self.km_reading)+" km on it")

    def update_km(self, km):
        if km >= self.km_reading:
            self.km_reading = km
        else:
            print("you cant roll back on km")


class ElectricCar(car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

    def des_battery(self):
        print("this car has "+str(self.battery)+" kwh battery")
    def fillGas(self):
        print("this car doesn't need gas")

class Battery():
    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        print("this car has a "+str(self.battery_size)+" kwh battery.")


my_car = ElectricCar("Audi", "V4", 2020)
print(my_car.getDes())
my_car.des_battery()
my_car.fillGas()
my_car.battery.describe_battery()

test = Battery(80)
test.describe_battery()

