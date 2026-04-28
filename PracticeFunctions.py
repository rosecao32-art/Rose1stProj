for number in range(1,6): 
    print(number)

def greet(name):
    return "Hello " + name
message = greet("Alice")
print(message)

text = "    python is fun   "
print(text.strip())
print(text.upper())
print(text.replace("python","Python"))

numbers = [1, 2, 3, 4, 5]
squares = [n * n for n in numbers]
print(squares)

try:
    number = int(input("Enter a number: "))
    print(10 / number)
except ZeroDivisionError:
    print("You cannot divide by zero.")
except ValueError:
    print("Please enter a valid number.")