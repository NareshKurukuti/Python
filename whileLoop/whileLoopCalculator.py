while True:
    print("enter a sum to sum of two numbers")
    print("enter a sub to sum of two numbers")
    print("enter a div to sum of two numbers")
    print("enter a mul to sum of two numbers")
    print("enter a exit or e for exiting")
    user_input = input('> ')
    if user_input == "exit" or user_input == "e":
        break
    elif user_input == "sum":
        a = float(input("please enter first number "))
        b = float(input("please enter second number "))
        c = a + b
    elif user_input == "sub":
        a = float(input("please enter first number "))
        b = float(input("please enter second number "))
        
        c = a - b
    elif user_input == "mul":
        a = float(input("please enter first number "))
        b = float(input("please enter second number "))
        
        c = a * b
    elif user_input == "div":
        a = float(input("please enter first number "))
        b = float(input("please enter second number "))
        
        c = a / b
    else:
        print('please enter sum or sub or div or mul or e or exit')
        continue

    print(f'the answer of {user_input} is {c}')

print("finish")
    
