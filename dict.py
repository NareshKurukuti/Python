welcome ="Hello World"
print(welcome)

my_dict = {"numbers_1" : [1,2,3,4], "numbers_2" : [2,3,4,5],"car_name" : "BMW"}

print("Using .keys() for dict")
for x in my_dict.keys():
    print(x)
    
print("Using .values() for dict")
for x in my_dict.values():
    print(x)
    
print("Using .items() for dict")
for x,y in my_dict.items():
        print(x,y)

print("Using .get() for dict")
getNames = my_dict.get("numbers_1")
print(getNames)

my_dict["numbers_1"]=['nares', 'kurukuti']
print(my_dict)
