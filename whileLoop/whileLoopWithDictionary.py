my_list1_active = ['root', 'admin', 'sorrow']
my_list2 = []

while my_list1_active:
    current_user = my_list1_active.pop()
    print("Verifying user: " + current_user)
    my_list2.append(current_user)
print("\n the following users have been confirmed")
for i in my_list2:
    print('__', i.title())


pets = ['dog', 'cat', 'dog', 'cat', 'rabbit', 'cat']

while 'cat' in pets:
    pets.remove("cat")
print(pets)


while True:
    print("enter a name")
    name = input()
    if name == 'exit' or name == 'e':
        break


print("repeat the questions")

res = {}

active = True
prompt = '>'
while active:
    print("please enter your name: ")
    name = input(prompt)
    response = input("please enter your date of birth: ")
    res[name]=response
    print("do your want to repeat the questions? ")
    repeat = input('yes/no')
    if repeat == "no":
        active = False
for k, v in res.items():
    print('_____', k, v)







