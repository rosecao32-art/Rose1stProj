def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero!"
    return a / b

while True:
    print("\nSimple Calculator")
    print("Choose an operation: +, -, *, / or q to quit")
    op = input("Operation: ")

    if op == "q":
        break

    try:
        a = float(input("Enter first number: "))    
        b = float(input("Enter second number: "))
    except ValueError:
        print("Invalid number. Try again.")
        continue

    if op == "+":
        print("Result:", add(a, b))
    elif op == '-':
        print("Result:", subtract(a, b))
    elif op == "*":
        print("Result:", multiply(a, b))
    elif op == "/":
        print("Result:", divide(a, b))
    else:
        print("Unknown operation. Try again.")
