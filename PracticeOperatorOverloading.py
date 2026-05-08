# + operator for integers
print(1 + 2)
# + operator for strings (concatenation)
print("Geeks" + "For")
# * operator for numbers
print(3 * 4)
# * operator for strings (repetition)
print("Geeks" * 4)

class A:
    def __init__(self, a):
        self.a = a
    # define behavior of +
    def __add__(self, o):
        return self.a + o.a 
ob1 = A(1)
ob2 = A(2)
ob3 = A("Geeks")
ob4 = A("For")
print(ob1 + ob2)   # integer addition
print(ob3 + ob4)   # string concatenation
# actual working (internally)
print(A.__add__(ob1, ob2))
print(ob1.__add__(ob2))

class Complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __add__(self, other):
        return self.a + other.a, self.b + other.b
Ob1 = Complex(1, 2)
Ob2 = Complex(2, 3)
Ob3 = Ob1 + Ob2
print(Ob3)

class A:
    def __init__(self, a):
        self.a = a
    def __gt__(self, other):
        return self.a > other.a
ob1 = A(2)
ob2 = A(3)
if ob1 > ob2:
    print("ob1 is greater than ob2")
else:
    print("ob2 is greater than ob1")

class A:
    def __init__(self, a):
        self.a = a
    def __lt__(self, other):
        return "ob1 is less than ob2" if self.a < other.a else "ob2 is less than ob1"
    def __eq__(self, other):
        return "Both are equal" if self.a == other.a else "Not equal"
ob1 = A(2)
ob2 = A(3)
print(ob1 < ob2)
ob3 = A(4)
ob4 = A(4)
print(ob3 == ob4)    

class MyClass:
    def __init__(self, value):
        self.value = value
    def __and__(self, other):
        return MyClass(self.value and other.value)
a = MyClass(True)
b = MyClass(False)
c = a & b  
print(c.value)
# c is an object of MyClass
print(c)