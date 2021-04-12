#In this example we can define constructor and self variables and compare of two object values
class Computer:

    def __init__(self):#It is a constructor
        self.name = "naresh" #self
        self.age = 20 #

    def compare(self, other):
        if self.age == other.age:
            return True
        else:
            return False


c1 = Computer()
print(c1.name)

c2 = Computer()
c2.age = 30
print(c2.name)

if c1.compare(c2):#c1 is self and c2 is other
    print("They are same")
else:
    print("They are different")