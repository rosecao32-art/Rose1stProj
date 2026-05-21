a = {"x": 1, "y": 2}
print(a)
b = dict(name="Sam", age=20)
print(b)

d = {'A': 10, 'B': 20}
k = d.keys()
d['C'] = 30
print(k)

d = {
    "student": {
        "name": "Sam",
        "age": 20
    }
}
print(d["student"]["name"])

i = 10
if i == 10:
    #  First if statement
    if i < 15:
        print("i is smaller than 15")
    # Nested - if statement
    # Will only be executed if statement above
    # it is true
    if i < 12:
        print("i is smaller than 12 too")
    else:
        print("i is greater than 15")
else:
  print("i is not equal to 10")

i = 25
 # Checking if i is equal to 10
if i == 10:
    print("i is 10")
# Checking if i is equal to 15
elif i == 15:
    print("i is 15")
# Checking if i is equal to 20
elif i == 20:
    print("i is 20")
# If none of the above conditions are true
else:
    print("i is not present")  

count = 0
while (count < 1):    
    count = count+1
    print(count)
    break
else:
    print("No Break")  

for i in range(3):
    print(i)
    break
else:
    print("Loop completed")     

# Python3 code to demonstrate working of 
# Iterating through value lists dictionary 
# Using list comprehension 
# Initialize dictionary 
test_dict = {'gfg' : [1, 2], 'is' : [4, 5], 'best' : [7, 8]} 
# printing original dictionary 
print("The original dictionary : " + str(test_dict)) 
# Using list comprehension 
# Iterating through value lists dictionary 
res = [[i for i in test_dict[x]] for x in test_dict.keys()] 
# printing result 
print("The list values of keys are : " + str(res))  

seq = {'a', 'b', 'c', 'd', 'e'}
# creating dict with default values as None
res_dict = dict.fromkeys(seq)
print("The newly created dict with None values : " + str(res_dict))
# creating dict with default values as 1
res_dict2 = dict.fromkeys(seq, 1)
print("The newly created dict with 1 as value : " + str(res_dict2))

d = {'a': 97, 'b': 98, 'c': 99, 'd': 100}
d.setdefault(' ', 32)
print(d)

d1 = {1: 10, 2: 20, 3: 30}
# Add items where the key is greater than 2
d2 = {k: v * 2 for k, v in d1.items() if k > 2}
print(d2)

d = {1: 10, 2: 20, 3: 30}
for i in range(4, 6):
    d[i] = i * 10  # Add new items in a loop
print(d)

d = {'Aman': 110, 'Rajesh': 440, 'Suraj': 990}
try:
    d["Kamal"]
    print('Found')
except KeyError as error:
    print("Not Found")

locals()['__builtins__']
print(locals())

###
#s = 'apple'
#try:
#    num = int(s)
#except ValueError:
#    raise ValueError("String can't be changed into integer")
###

s = 'apple'
try:
    num = int(s)
except ValueError:
    raise ValueError("String can't be changed into integer")