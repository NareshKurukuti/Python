def findPrime(n):
    prime = True
    for i in range(2,n):
        if n % 2 ==0 :
          prime = False
    return prime

print(findPrime(10))


for i in range(2,200):
    if findPrime(i):
        print(i, 'is a prime')
    else:
        print(i, 'is not a prime')

"""
Fibanacci series 1 2 3 5 8 13 21
"""
first = 1
second = 2
for i in range(1,10):
    print(first)
    new = first + second
    first = second
    second = new




