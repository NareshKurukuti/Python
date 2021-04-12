print("#example map() with normal function")
def add_five(x):
    return x + 5

nums = [11,22,33,44,55,66,77,88,99]
results = list(map(add_five, nums))
print(results)


print("#example map() with lambda function")
resultsNew = list(map(lambda x:x+5, nums))
print(resultsNew)

#example of filter() with normal function
def add_filter(x):
    if x %2 == 0:
        return x
resultsNow = list(filter(add_filter, nums))
print(resultsNow)

#example of filter() with lambda function
print("#example of filter() with lambda function")
resultsOfFilter = list(filter(lambda x: x % 2==0, nums))
print(resultsOfFilter)
