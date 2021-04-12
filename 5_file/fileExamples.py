f = open('test.txt', 'r')
file_1 = f.read()
print(file_1)

f = open("test.txt", 'w')
f.write("Hello World\n")
f.close()


f = open('test.txt', 'r')
file_1 = f.read()
print(file_1)


"""example with open as """
with open("test.txt","w") as file:
    file.write("Hi \n Hellow World \n bye")
file.close()

with open("test.txt") as f:
    f = f.read()
print(f)
