for number in range(1,6): 
    print(number)

def greet(name):
    return "Hello " + name
message = greet("Alice")
print(message)

def add(a, b=0):
    return a + b
print(add(5,9))

def say_hello():
    print("Hello")
say_hello()    

def greet(name):
    print("Hello", name)
greet("Alex")    

def add_numbers(a, b):
    return a + b
result = add_numbers(3, 5)
print(f"Result is {result}")

def is_even(number):
    return number % 2 == 0
print(f"Number 9 for even number test: {is_even(9)}")

def show_welcome():
    print("Welcome")
    print("Please log in")
show_welcome()  

text = "    python is fun   "
print(text.strip())
print(text.upper())
print(text.replace("python","Python"))

tasks = ["Write code", "Test program", "Deploy app"]
for index, task in enumerate(tasks, 1):
    print(f"{index}. {task}")

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