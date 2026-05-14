print("Multi-line Strings:-------") 
s = """I am Learning
Python String on GeeksforGeeks"""
print(s)
s = '''I'm a 
Geek'''
print(s)

print("Access specific characters through positive indexing:-------") 
s = "GeeksforGeeks"
print(s[0])   
print(s[4])

print("Read characters from the end using negative indices:-------")
s = "GeeksforGeeks"
print(s[-10])  
print(s[-5])

print("String Slicing:-------")
s = "GeeksforGeeks"
print(s[1:4])    
print(s[:3])     
print(s[3:])    
print(s[::-1])
print("Access elements from the end of a string using negative indices:---")
text = "Python"
print(text[-1])
print(text[-3])
print("Ways to Perform Negative Slicing:---")
print("Using Colon Operator:--")
text = "GeeksforGeeks"
# Slicing left part of string text
left = text[:-8]
# Slicing middle part of string text
middle = text[-8:-5]
# Slicing right part of string text
right = text[-5:]
print(left)
print(middle)
print(right)
print("Using slice function:--")
text = "GeeksforGeeks"
# Slicing left part of string text
left = text[slice(-8)]
# Slicing middle part of string text
middle = text[slice(-8, -5)]
# Slicing right part of string text
right = text[slice(-5, None)]
print(left)
print(middle)
print(right)
print("Slicing List with Negative Numbers:---")
li = ["pen", "pencil", "eraser", "apple", "guava", "ginger","Potato", "carrot", "Chilli"]
a = li[-4:]
print(a)
b = li[slice(-6, -4)]
print(b)
print("Reverse List with the Negative Step:---")
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
rev = num[::-1]
print(rev)
rev2 = num[slice(None, None, -1)]
print(rev2)
print("Slicing Alternates in the List with Negative Step:---")
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
alt = num[::-2]
print(alt)
alt2 = num[slice(None, None, -2)]
print(alt2)
print("Slicing Tuples with Negative Numbers:---")
tup = (1, 2, 3, 4, 5, 6, 7, 8, 9)
s = tup[-3:]
print(s)
s = tup[-5:-2]
print(s)
rev_tup = tup[::-1]
print(rev_tup)
s = tup[::-2]
print(s)

print("String Iteration:-------")
s = "Python"
for char in s:
    print(char)

print("String Immutability:-------")
s = "geeksforGeeks"
s = "G" + s[1:]  
print(s)

print("Deleting a String:-------")
s = "GfG"
del s
print("Del Keyword for Deleting Objects:---")
class Gfg_class:
    a = 20
# creating instance of class
obj = Gfg_class()
# delete object
del obj
# we can also delete class
del Gfg_class
print("Deleting Variables:---")
a = 20
b = "GeeksForGeeks"
# delete both the variables
del a, b
# check if a and b exists after deleting
# print(a), NameError: name 'a' is not defined
# print(b), NameError: name 'b' is not defined
print("List Slicing Using del Keyword:---")
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# delete second element of 'a'
del a[1]
# check if the second element in 'a' is deleted
print(a)
# slice 'a' from index 3 to 5
del a[3:5]
# check if the elements from index 3 to 5 in 'a' is deleted
print(a)
print("Deleting Dictionary and Removing key-value Pairs:---")
d = {"small": "big", "black": "white", "up": "down"}
# delete key-value pair with key "black" from my_dict1
del d["black"]
# check if the  key-value pair with key "black" from d1 is deleted
print(d)

print("Updating a String:-------")
s = "hello geeks"
s1 = "H" + s[1:]                  
s2 = s.replace("geeks", "GeeksforGeeks")  
print(s1)
print(s2)
print("Updated new string:-------")
s = "Python is fun. Python is powerful."
res = s.replace("Python", "Coding")
print(res)

print("Common String Methods:-------")
print("len:---")
s = "GeeksforGeeks"
print(len(s))
print("upper/lower:---")
s = "Hello World"
print(s.upper())
print(s.lower())
print("strip/replace:---")
s = "   Gfg   "
print(s.strip())    
s = "Python is fun"
print(s.replace("fun", "awesome"))

print("Concatenating and Repeating Strings:-------")
print("Join two words with a space:---")
s1 = "Hello"
s2 = "World"
print(s1 + " " + s2)
print("Repeat a greeting three times:---")
s = "Hello "
print(s * 3)

print("Formatting Strings:-------")
print("Using f-strings:---")
name = "Jake"
age = 22
print(f"Name: {name}, Age: {age}")
print("Using format:---")
s = "My name is {} and I am {} years old.".format("Emily", 22)
print(s)

print("String Membership Testing:-------")
s = "GeeksforGeeks"
print("Geeks" in s)
print("GfG" in s)