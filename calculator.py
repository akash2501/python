
print("hello!!")
print("This is a basic calculator")
print("1. Addition")
print("2. Multiplication")
print("3. Division")
print("4. Subtraction")
print("5. Exit")
c=0
while True:
    op = input("what you want to do >>")

    if op == "1":
        a = float(input("enter first number>"))
        b = float(input("Enter second number>"))
        c = a + b
        print("Addtion is",c)
    elif op == "2":
        a = float(input("Enter First number>"))
        b = float(input("Enter Second number>"))
        c = a*b
        print("Multiplication is",c)
    elif op == "3":
        a = float(input("Enter First number>"))
        b = float(input("Enter Second number>"))
        c = a/b
        print("Devision is",c)
    elif op== "4":
        a = float(input("Enter First number>"))
        b = float(input("Enter Second number>"))
        c = a - b
        print("Subtraction is", c)
    elif op == "5":
        print("Thank You!!")
        break
    else:
        print("PLease give proper operation")



