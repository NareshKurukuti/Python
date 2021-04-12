
a = 5
b = 1

try:
    print("Resource open")
    print(a/b)
    k = int(input("Enter a number"))
    print(k)

except ZeroDivisionError as e:
    print("Hey, You cannot divide a Number by zero", e)

except ValueError as e:
    print("invalid input")

except Exception as e:
    print("Something went wrong.....")
    print(e)

finally:
    print("Resource closed")