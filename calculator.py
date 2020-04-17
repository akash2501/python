
print("hello!!")
print("This is a basic calculator")
print("1. Addition")
print("2. Multiplication")
print("3. Division")
print("4. Subtraction")
print("5. Percentage")
print("6. Modulus")
print("7. Exit")
c=0
def add(x,y):
    c = a +b
    print("Addition is",c)

while True:
    op = input("what you want to do >>")

    if op == "1":
        a = float(input("enter first number>"))
        b = float(input("Enter second number>"))
        add(a,b)
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
    elif op == "4":
        a = float(input("Enter First number>"))
        b = float(input("Enter Second number>"))
        c = a - b
        print("Subtraction is", c)
    elif op == "5":
        a = float(input("Enter First number>"))
        b = float(input("Enter Second number>"))
        c = (a/b)*100
        print("Percentage of 1st with respect of 2nd is", c)
    elif op == "6":
        a = float(input("Enter First number>"))
        b = float(input("Enter Second number>"))
        c = a%b
        print("remainder is", c)
    elif op == "7":
        print("Thank You!!")
        break
    else:
        print("PLease give proper operation")



