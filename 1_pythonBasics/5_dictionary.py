# Dictionary:  It is a like key and value pair.
# Key is immutable and unique.
#

data = {1: "naresh", 2: "kurukuti", 3: "nk"}
print(data)

print("\n print the type")
print(type(data))

print("\n get the dict data based on index")
print(data[2])

print("\n to get data using .get() in dict")
print(data.get(1))

print("\n assing the value for not specified keys")
print(data.get(0, "Not Found"))


print("\n To add two list as dictionary")
keys = ['naresh','kurukuti', 'nk']
values = ['Python', 'php', 'Java']
data = dict(zip(keys, values))
print(data)

print("\n assign new key and value to dictionary")
data['kn'] = 'JS'
print(data)

print("\n delete key and values in dict")
del data['nk']
print(data)

print("\n list in dictionary and dictionary in dictionary")
prog = {'JS': 'Atom', 'CS': 'VS', 'Python': ['Pycharm', 'Sublime'], 'Java': {'JSE':'Netbeans', 'JEE': 'Eclipse'}}
print(prog)
print(type(prog))
print(prog['Python'])
print(prog['Java'])
print(prog['Java']['JEE'])