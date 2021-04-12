"""
TypeCode    CType          PythonType
'b'         signed          int
'B'         unsigned char   int
'u'         Py_UNICODE      Unicode Character
'h'         signed short     int
'H'         UnSigned Short   int
'i'         Signed int       int
'I'         UnSigned int     int
'l'         Signed long      int
'L'         UnSigned Long    int
'f'         Float            float
'd'         Double           float

"""
from array import *

from numpy import zeros
from numpy.core import ones


vals = array('i', [5,9,5,8,4])#here i means integer array

print(vals)

print("\n Output of buffer info")
print(vals.buffer_info())

print("\n toget the array typecode")
print(vals.typecode)

print("\n to change the array values in reverse order")
vals.reverse()
print(vals)

print("\n creating new array with existing array")

newArray = array(vals.typecode, (a*a for a in vals))
print(newArray)

print("\n Creating array from the user")
arr2 = array('i',[])

n = int(input("Enter the lenght of array"))

for i in range(n):
    x = int(input("Enter the next value"))
    arr2.append(x)

print(arr2)

print("\n to get the index of array value using .index()")
print(arr2.index(1))

"""
# array()
# linspace()
# logspace()
# arange()
# zeros()
# ones()
"""
from numpy import *

arr = array([1,2,3,4,5.0])#implict conversion : means in the array one element is float so it will convert the entire array into float
print(arr.dtype)


print("\n example linspace()")
als = linspace(0,15,25)#linspace(start,stop,range)=> means in given range it will create mention range number of parts
print(als)

print("\n example of logspace()")
ls = logspace(1,40,5)
print(ls)

print("\n example of zeros()")
zs = zeros(5)
print(zs)

print("\n example of ones()")
os = ones(22)
print(os)