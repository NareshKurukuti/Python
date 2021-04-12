#Method Overloading means in the class two methods with the same name and difference parameters is called Method Overloading
#In Python there is no Method Overloading


#Method Overriding: means in the class two method with the same name and same no.of parameters is called Method Overriding
class A:
    def show(self):
        print("in A show")

class B(A):
    def show(self):
        print("in B show")

b = B()
b.show()