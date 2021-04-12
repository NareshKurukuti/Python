#List:  List are mutable and square bracket is used for Lists
nums = [12,45, 35, 23, 34, 55]

print(nums)
print(nums[0])
print(nums[-1])
print(nums[1:2])


names = ["naresh", "nar", "kn", "nk"]
print(names)

values = [9.5, "naresh", 26]
print(values)

print("\n multiple lists in single lists")
mil = [nums, names]
print(mil)

print("\n append")
nums.append(77)
print(nums)

print("\n insert a value at the index of 2")
nums.insert(2, 22)
print(nums)

print("\n remove the list value based on index")
nums.remove(nums[0])
print(nums)

print("\n remove the list value based on value")
nums.remove(45)
print(nums)

print("\n remove the list value based on index using pop")
nums.pop(1)
print(nums)

print("\n remove the last value in the list using pop")
nums.pop()
print(nums)

print("\n delete or remove the multiple values in the list")
del nums[2:]
print(nums)

print("\n add multiple values in list")
nums.extend([12,44,35,79])
print(nums)

print("\n in built functions in list like min()")
print(min(nums))

print("\n in built functions in list like max()")
print(max(nums))

print("\n in built functions in list like sort()")
nums.sort()
print(nums)

print("\n clear() of the list")
nums.clear()
print(nums)


