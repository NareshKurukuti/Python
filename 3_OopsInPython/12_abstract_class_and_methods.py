#We can declare a method but not define the method, that method is called Abstract methods.
#A class contain abstract methods, that is called Abstract Class.
from abc import ABC,abstractmethod

class Computer(ABC):

    @abstractmethod
    def process(self):
        pass

class Laptop(Computer):

    def process(self):
        print("its running")

class Programmer:
    def work(self, com):
        print("Solving Bugs")
        com.process()

com1 = Laptop()
# com1.process()

pg = Programmer()
pg.work(com1)