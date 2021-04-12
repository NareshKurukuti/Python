# Types of Methods:
# Instance Methods: A method to do with instance variables is called Instance Method.
# Class Methods: A method to do certain behaviour with class variables is called Class Method.  We can use the @classmethod decorator for the Class Methods.
# Static Methods: A method has nothing to do with instance variables and also nothing to do with class variables.  We can use the @staticmethod decorator for the Static Methods.
#
# In Instance methods itself, it has two types, such as Accessors and Mutator methods.
# An accessor is getting the values and Mutators are set the values.

class Student:

    school = "TechSchool"

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    #These are the Instance Methods
    def get_m1(self):
        return self.m1

    def set_m1(self, m1):
        self.m1 = m1
        return self.m1

    def avg(self):
        return (self.m1+self.m2+self.m3)/3

    #This is Class Method
    @classmethod
    def getSchool(cls):
        return cls.school

    #This is Static Method
    @staticmethod
    def info():
        print("This is Static Method..")

s1 = Student(30,40,80)

s2 = Student(50, 49, 77)
s2.set_m1(90)

print(s1.avg())
print(s2.avg())