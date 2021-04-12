#normal function
def test(x):
    return x**2+5*x+4
print(test(-4))

#lambda function
print((lambda x: x**2+5*x+4)(-4))

a = (lambda x: x*x)(40)
print(a)


triple = lambda x:x *3
add = lambda x,y : x + y
print(triple(3))

print(add(3,3))


def myfunc(n):
    return lambda a : a *n

mydoubler = myfunc(2)
mytripler = myfunc(3)
print(mydoubler(11))
print(mytripler(11))
