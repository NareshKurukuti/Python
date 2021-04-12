class Car:
    wheels = 4 #this is class variables

    def __init__(self):
        self.mil = 10 #this is instance variables
        self.com = "BMW"#this is instance variables


c1 = Car()
c2 = Car()#Class namespace

print(c1.mil, c1.com, Car.wheels)
print(c2.mil, c2.com, c2.wheels)
c2.mil = 8 #object/instance namespace
print(c2.mil, c2.com, c2.wheels)

