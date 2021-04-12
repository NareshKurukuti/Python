#Single Inheritance
class A:
    def feature1(self):
        print("Feature1 working")

    def feature2(self):
        print("Feature2 working")

class B(A):
    def feature3(self):
        print("Feature3 working")

    def feature4(self):
        print("Feature4 working")

a = A()
print("Single Inheritance")
a.feature1()

#Multilevel Inheritance
class One:
    def feature1(self):
        print("MI Feature1 working")

    def feature2(self):
        print("MI Feature2 working")

class Two(One):
    def feature3(self):
        print("MI Feature3 working")

    def feature4(self):
        print("MI Feature4 working")

class Three(Two):
    def feature5(self):
        print("MI Feature5 working")

    def feature6(self):
        print("MI Feature6 working")

o = Three()
print("Multilevel Inheritance")
o.feature1()

#Multiple Inheritance

class Aone:
    def feature1(self):
        print("mul feature1 working")

    def feature2(self):
        print("mul feature2 working")

class Atwo:
    def feature3(self):
        print("mul feature3 working")

class Athree(Aone, Atwo):
    def feature4(self):
        print("mul feature4 working")

mul_inheritance = Athree()
print("Multiple Inheritance")
mul_inheritance.feature3()