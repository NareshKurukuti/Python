from functools import reduce
#Example of Filter
print("Example of Filter")
nums = [2,3,23,3,4,5,6]
evens = list(filter(lambda n:n%2==0,nums))
print(evens)

#Example of Map
print("\n Example of Map")
doubles = list(map(lambda n:n*2, evens))
print(doubles)

#Example of reduce
print("\n Example of Doubles")
sum = reduce(lambda a,b: a+b, doubles)
print(sum)