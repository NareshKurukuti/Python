class Computer:

    def __init__(self,cpu,ram):
        self.cpu = cpu
        self.ram = ram
        print("in init")

    def config(self):
        print("Config is",self.cpu,self.ram)


com1 = Computer("i5","16gb")
com2 = Computer("Razen", "32Gb")

com1.config()
com2.config()
