
f = open("MyData", "r")

print(f.readline(), end="#")
print(f.readlines())

f1 = open("abc", "w")
f1.write("Something")


f1 = open("abc", "r")

print(f1.read())



#Copy Image
ci = open("dolls.png", "rb")

cin = open("dolls_new.png", "wb")

for i in ci:
    cin.write(i)