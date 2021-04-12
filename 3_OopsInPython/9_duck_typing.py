class Pycharm:
    def execute(self):
        print("Compiling")
        print("running")

class MyEditor:
    def execute(self):
        print("spellcheck")
        print("convention check")
        print("compiling")
        print("running")

class Laptop:
    def code(self,ide):
        ide.execute()

ide = MyEditor()
ide2 = Pycharm()
lap1 = Laptop()
lap1.code(ide)
lap1.code(ide2)