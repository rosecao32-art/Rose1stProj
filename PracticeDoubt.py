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