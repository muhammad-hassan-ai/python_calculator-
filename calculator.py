#Addition
def add (a=0,b=0):
    return a+b

#Subtraction
def sub(c=0,d=0):
    return c-d

#Multiplication
def mul(a=0,b=0):
    return a*b

#Division
def dev(a=0,b=0):
    if b == 0:
        return "Error: Cannot divide by zero."
    else:
        return a/b


while True:

    try:
        num1 = float(input("\nEnter first number: "))
        op =input("Enter operator: ")
        num2 = float(input("Enter second number: "))

        
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        continue


    if op == "+":
        print(add(num1,num2))

    elif op == "-":
        print(sub(num1,num2))

    elif op == "*":
        print(mul(num1,num2))

    elif op == "/":
        print(dev(num1,num2))
        

    else:
        print("Invalid operator. Please enter +, -, *, or /.")



