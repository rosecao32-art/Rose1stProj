# Prints all letters except 'e' and 's'
i = 0
a = 'geeksforgeeks'
while i < len(a):
    if a[i] == 'e' or a[i] == 's':
        i += 1
        continue
    print(a[i])
    i += 1
print("\n")
# Using continue to skip an iteration
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)

i = 0
a = 'geeksforgeeks'
while i < len(a):
    if a[i] == 'e' or a[i] == 's':
        i += 1
        break
    print(a[i])
    i += 1
i = 0
while i < 4:
    i += 1
    print(i,"\n")
    break
else:  # Not executed as there is a break
    print("No Break")
# Using break to exit the loop
for i in range(10):
    if i == 5:
        break
    print(i)  

a = 'geeksforgeeks'
i = 0
while i < len(a):
    i += 1
    pass
print('Value of i :', i)   
# Using pass as a placeholder
for i in range(5):
    if i == 3:
        pass  
    print(i) 

i = 0
while i < 4:
    i += 1
    print(i)
else:  # Executed because no break in for
    print("No Break\n")

# Iterating over a list
print("Iterating over a list")
a = [1, 2, 3]
for i in a:
    print(i)    
print("Reverse order for-in loop")    
bs = [7, 8, 9]    
for b in reversed(bs):
    print(b)
print("Reverse order while loop")
c = [10, 20, 30]
i = len(c) - 1
while i >= 0:
    print(c[i])
    i -= 1

    
    