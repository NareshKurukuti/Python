#Operators:
"""
1. Arithmetic Operators
2. Assignment Operators
3. Relational Operators
4. Logical Operators
5. Unary Operators
6. Bitwise Operators

"""

#Arithmetic Operators
print('\n Arithmetic Operators')
x, y = 5, 3
print(x+y)
print(x-y)
print(x*y)
print(x/y)

#Assignment Operators
print('\n Assignment Operators')
j = 2

j += 2 #increment by 2
print(j)

j *= 3
print(j)

#Unary Operators
print('\n Unary Operators')
n = 7
n = -n  #-sign is unary operator
print(n)

#Relational Operators >,<,<=,>=,==,!=
print('\n Relational Operators')
a,b = 5,9

if a > b:
    print(True)
else:
    print(False)

#Logical Operators: and,or,not
print('\n Logical Operators')
k = 5
l = 8

if k < 10 and l <12:
    print(True)
else:
    print(False)


#Bitwise Operators: Complement(~), And(&), Or(|), Xor(^), Left Shift(<<), Right Shift(>>)
print('\n Bitwise Operators')
print('\n ~ (complement) operator output')
x = 12
print(~x)# '~' it will gives the 2's complement output

print('\n & (and) operator output')
x = 11
y = 19
print(x&y)

print('\n | (or) operator output')
print(x|y)

print('\n ^ (xor) operator output')
print(x^y)

print('\n << (leftshift) operator output')
print(x<<2)

print('\n >> (rightshift) operator output')
print(x>>2)

