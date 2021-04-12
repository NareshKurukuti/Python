class Test():
    def __init__(self, list1):
        self.list1 = []
        self.list2 = list1

    def printList(self):
        for i in self.list1:
            print('_', i)

    def printList2(self):
        for i in self.list2:
            print('_list2', i)
    def appendList(self, l):
        for i in l:
            self.list1.append(i)
            
my_list = Test(['Naresh', 'K', '26'])

my_list.appendList(['test', 'test2'])

my_list.printList()

my_list.printList2()



"""split the string and move into the list """
print("\n\n\nExample Two")
class split():
    def __init__(self, l):
        self.l = l

    def printList(self):
        if type(self.l) == type(''):
            s = (self.l).split()
            print(s, ' is list')
            for i in s:
                print('_', i)
        elif type(self.l) == type([]):
            print(self.l, ' is list')
            for i in self.l:
                print('_', i)
    def splitData(self):
        s = (self.l).split()
        print(s)

split = split("hi this is python")
split.printList()
split.splitData()
