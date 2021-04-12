fileName = "D:/#Python/file/test.txt"

#example for read data for the file take
with open(fileName, 'r') as file:
     file = file.read()
print(file)


#example for readline()

with open(fileName, 'r') as file:
     file = file.readlines()
print(file)


#example for write the data into file
with open(fileName, 'w') as file:
    file.write("test One")
    file.write("test two")
    file.write("test three")
file.close()

with open(fileName, 'r') as f:
    f = f.read()
print(f)
