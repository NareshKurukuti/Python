#When we can use super() it will take from the left to right of the parent class
class A:
    def __init__(self):
        print("in A Init")

    def feature1(self):
        print("Feature1-A working")

    def feature2(self):
        print("Feature2-A working")

class B:
    def __init__(self):
        super().__init__()
        print("in B Init")

    def feature1(self):
        print("Featue1-B working")

    def feature2(self):
        print("Feature2-B working")


class C(B,A):
    def feature1(self):
        print("Feature1-C working")

    def feature2(self):
        super().feature2()
        print("Feature2-C working")


a = C()
a.feature2()
