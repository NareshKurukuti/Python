from itertools import accumulate, takewhile, product

nums = list(accumulate(range(8)));
print(nums)

num_takewhile = list(takewhile(lambda x : x<=6, nums))
print(num_takewhile)

letter = ['a', 'b']
print(list(product(letter, range(2))))

