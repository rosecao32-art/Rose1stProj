import math, datetime
import keyword

def main():
    name = "Alice"
    age = 25
    height = 5.6
    is_student = True
    name = input("Enter your name: ")
    print ("Hello", name)

    name = "Alice"
    score = 95
    print(f"Student {name} scored {score} marks.")

    x, y = 5, 3
    print(f"Sum: {x + y}, Product: {x * y}")

    print(f"Pi rounded to 3 decimals: {math.pi: .3f}")
    today = datetime.date.today()
    print(f"Today is {today:%B %d, %Y}")
    
    fruits = ["apple", "banana", "cherry"]
    print(fruits[0])
    print(fruits[1])

    user = {"name": "Alice", "age": 25, "is_member": True}
    print(user["name"])
    print(user["age"])

    age = 18
    if age >= 18: print("You are allowed to vote.")

    temperature = 15
    if temperature > 20: print("It's warm outside.")
    else: print("It's cold outside.")

    score = 82
    if score >= 90:
        print("Grade: A")
    elif score >= 80:
        print("Grade: B")
    elif score >= 70:
        print("Grade: C")
    else:
        print("Grade: F")

    is_logged_in = True
    is_admin = False
    if is_logged_in:
        if is_admin:
            print("Welcome, admin.")        
        else:
            print("Welcome, user.")
    else:
        print("Please log in.")

    age = 25
    has_id = True
    if age >= 18 and has_id:
        print("Entry allowed.")
    else:
        print("Entry denied.")

    age = 16
    status = "Adult" if age >= 18 else "Minor"
    print(status)

    print("The list of keywords are: ")
    print(keyword.kwlist)
    num = 10
    print(num)
    print(keyword.iskeyword('rose'))

    a = 15
    b = 4
    print("Additon:", a + b)
    print("Subtraction:", a - b)
    print("Multiplication:", a * b)
    print("Division:", a / b)
    print("Floor Division:", a // b)
    print("Modulus:", a % b)
    print("Exponentiation:", a ** b)

    res = 10 / 3
    print(res)
    print(type(res))
    res = 10 // 3
    print(res)
    print(type(res))
    print(-17 / 5)
    print(-17 // 5)

    a = 13
    b = 33
    print(a > b)
    print(a < b)
    print(a == b)
    print(a != b)
    print(a >= b)
    print(a <= b)

    a, b, c = True, False, True
    # AND: Both conditions must be True
    if a and c:
        print("Both a and c are True (AND condition).")
    # OR: At least one condition must be True
    if b or c:
        print("Either b or c is True (OR condition).")
    # NOT: Reverses the condition
    if not b:
        print("b is False (NOT condtion).")
            

main()