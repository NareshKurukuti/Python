i = 0
while i < 10:
    print(i)
    i=i+1


print("To Print Event Numbers upto 100")
while i < 100:
    if i % 2 == 0 :
        print(i)
    i=i+1


name = "naresh KURUKUTI"
i = 0
while i < len(name):
    print(name[i])
    if name[i] == "K":
        break
    i += 1


print("Continue and Break command")
i = 0
while True:
    i += 1
    if i == 2:
        print('skipping 2')
        continue
    if i == 5:
        print('now break')
        break
    print(i)
print('finish')


    
