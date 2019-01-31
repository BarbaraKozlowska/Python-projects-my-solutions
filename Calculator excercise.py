#This calculator accepts only numbers, any non-numeric input will cause calculator to fail

def get_number(prompt):
    while True:
        number=float(input(prompt))

        if number !=0.0:
            return number
        else:
            print("0 is not an acceptable number")

def get_operator():
    while True:
        operator=input("Input one of the following operator: +, -, *, /")
        if operator=="+" or operator=="-" or operator=="*" or operator=="/":
            return operator
        else:
            print(operator, "is not valid operator")

def perform_calc(op,x,y):
    if op=="+":
        return x+y
    elif op=="-":
        return x-y
    elif op=="*":
        return x*y
    else:
        return x/y

while True:
    print("To perform a calculation, enter two numbers and an operator.")

    num1=get_number("Enter first number:")
    num2=get_number("Enter second number:")
    op=get_operator()
    val=perform_calc(op,num1,num2)

    print("Result:", val)

    response=input("Would you like to perform another operation? (YES/NO)")

    if response !="YES":
        print("Ok, Goodbye.")
        break
    
