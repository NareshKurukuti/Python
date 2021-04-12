#id() function is used to get the address of the memory

num = 5
print(id(num))

name = "naresh"
print(id(name))

a = 10
b = a
print(id(a))
print(id(b))

#DataTypes:

"""
1. None
2. Numeric: int, float, complex, bool
3. List
4. Tuple
5. Set
6. String
7. Range
8. Dictionary
"""

#Numeric:
num = 5
print(type(num))

numf = 2.5
print(type(numf))

numc = 6+9j
print(type(numc))

bl = True
print(type(bl))

#convert one format to another format
num = float(5)
print(type(num))

a,b = 5,4
com = complex(a,b)
print(type(com))

print(int(True))

print(int(False))

#Range
print(list(range(10)))

print(list(range(2,10,2)))

