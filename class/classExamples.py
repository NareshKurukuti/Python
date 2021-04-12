"""
Example One
"""

class Test():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def sit(self):
        print(self.name.title() + ' is now sitting')

    def sit2(self):
        print(self.name.title(), str(self.age))


m = Test('naresh', 26)
m.sit()
m.sit2()

person1 = Test("person1", 25)
person2 = Test("person2", 26)


person1.sit()
person1.sit2()


person2.sit()
person2.sit2()


"""
Example about Cars
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
my_new_car = car('Audi', 'a4', 2020)

print(my_new_car.getDes())
my_new_car.update_km(30)
print(my_new_car.read_km())
