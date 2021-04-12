print("give two number i will divide them")
print("enter e or exit to exit")

while True:
    firstNumber = input('enter first number ')
    if firstNumber == "e" or firstNumber == "exit":
        break
    secondNumber = input('enter second number ')
    if secondNumber == "e" or secondNumber == "exit":
        break
    try:
        answer = int(firstNumber)/int(secondNumber)
        print(answer)
    except ZeroDivisionError:
        print('the answer is 0 or zero')

