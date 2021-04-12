def getName(name):
    print('Hi '+name)

print("enter yourname")
getName(input())


print("validate the phone number in the format of 000-000-0000")

def validatePhoneNumber(number):
    if len(number)!=12:
        return False
    for i in range(0,3):
        if not number[i].isdecimal():
            return False
    if number[3] != "-":
        return False
    for i in range(4,7):
        if not number[i].isdecimal():
            return False
    if number[7] !="-":
        return False
    for i in range(8,12):
        if not number[i].isdecimal():
            return False
    return True


message = "call me at 415-555-1011 tomorrow. 415-555-9999 is my office"

for i in range(len(message)):
    test = message[i:i+12]
    if validatePhoneNumber(test):
        print('phone number found: '+ test)

print('Done')
