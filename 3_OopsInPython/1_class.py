class Computer:

    def config(self):
        print("i3 8Gb 1TB")


com1 = Computer()
com1.config() # way of accessing methods
Computer.config(com1) #way of accessing methods # in this com1 is argument

com2 = Computer()
com2.config()
