"""
yield in python is keyword, which is used
to return from a function without destroying the
states of its local variable and when function is called,
the execution starts from the yield statement.  Any function
that contains a yield keyword is termed as generator.
"""

def countDown(x):
    for i in range(x):
        if i %2 == 0:
            yield i

print(countDown(20))
print(list(countDown(10)))
