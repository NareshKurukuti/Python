class Student:

    def __init__(self, name,rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.Laptop()

    def show(self):
        print(self.name, self.rollno)
        self.lap.show()


    class Laptop:

        def __init__(self):
            self.brand = "Lenvo"
            self.cpu = "i7"
            self.ram = 8

        def show(self):
            print(self.brand, self.cpu,self.ram)


s1 = Student("naresh", 20)
# s2 = Student("k", 22)

# print(s1.show())
# print(s2.show())

# lap = Student.Laptop()
s1.show()