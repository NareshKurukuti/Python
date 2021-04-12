#break example
av = 5

x = int(input("How many Candies you want?"))

i = 1
while i <= x:

    if i > av:
        print("Out of Stock")
        break

    print("Candy")
    i += 1

print("Bye")

#Contine keyward example (to print values which is not   divisable by 3 or 5)
print("\n Contiune example")
for i in range(1, 10):
    if i%3 == 0 or i%5 ==0 :
        continue

    print(i)

print("Bye")

#Example for Pass (To print only even numbers)
print("\n Pass Example")
for i in range(1,10):
    if i%2 != 0:
        pass
    else:
        print(i)

print("Bye")

