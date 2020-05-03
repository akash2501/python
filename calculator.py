
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
    c = x + y
    print("Addition is",c)

def multiply(x,y):
    c = x*y
    print("Multiplication is",c)
def divide(x,y):
    c = x/y
    print("Division is",c)
def subtract(x,y):
    c = x - y
    print("Subtraction is",c)
def percent(x,y):
    c = (x/y)*100
    print("Percentage of A with respect to B is",c,"%")
def remainder(x,y):
    c = x%y
    print("Remainder of 1st when divided with 2nd is",c)
while True:
    op = input("what you want to do >>")

    if op == "1":
        a = float(input("enter first number>"))
        b = float(input("Enter second number>"))
        add(a,b)
    elif op == "2":
        a = float(input("Enter First number>"))
        b = float(input("Enter Second number>"))
        multiply(a,b)

    elif op == "3":
        a = float(input("Enter First number>"))
        b = float(input("Enter Second number>"))
        divide(a,b)
    elif op == "4":
        a = float(input("Enter First number>"))
        b = float(input("Enter Second number>"))
        subtract(a,b)
    elif op == "5":
        a = float(input("Enter First number>"))
        b = float(input("Enter Second number>"))
        percent(a,b)
    elif op == "6":
        a = float(input("Enter First number>"))
        b = float(input("Enter Second number>"))
        remainder(a,b)
    elif op == "7":
        print("Thank You!!")
        time.sleep(5)
        break
    else:
        print("PLease give proper operation!")



