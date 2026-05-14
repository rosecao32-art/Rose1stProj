print("Using delattr() to delete an object attribute in Python -------") 
class Equation:
  x = 3
  y = -8
  z = 5
l1 = Equation()
print("Value of x = ", l1.x)
print("Value of y = ", l1.y)
print ("Value of z = ", l1.z)
delattr(Equation,'z')
print ("Value of x = ", l1.x)
#print ("Value of y = ", l1.z)

print("Python delattr() Example 1 -------") 
class course:
    name = "data structures using c++"
    duration_months = 6
    price = 20000
    rating = 5
# creating an object of course
print(course.rating)
# deleting the rating attribute from object
delattr(course, 'rating')
# checking if the rating attribute is there or not
try:
    print(course.rating)
except Exception as e:
    print(e)

print("Python delattr() Example 2 -------")     
class course:
    name = "data structures using c++"
    duration_months = 6
    price = 20000
    rating = 5
# creating an object of course
print(course.price)
# deleting the price attribute from object
delattr(course, 'price')
# checking if the price attribute is there or not
try:
    print(course.price)
except Exception as e:
    print(e)

print("Using the delattr() method -------")
class Geek:
    domain = "geeksforgeeks.org"
if __name__ == '__main__':
    geeks = Geek()
    print("Before deleting domain attribute from geeks object:")
    print(geeks.domain)
    #delattr(geeks, "domain")
    #print("After deleting domain attribute from geeks object:")
    # this will raise AttributeError if we try to access 'domain' attribute
    #try:
    #    print(geeks.domain)    
    #except Exception as e:
    #    print(e)

print("Using the del method -------")        
class Geek:
    domain = "geeksforgeeks.org"
if __name__ == '__main__':
    geeks = Geek()
    print("Before deleting domain attribute from geeks object:")
    print(geeks.domain)
    # using del operator
    #del geeks.domain
    #print("After deleting domain attribute from geeks object:")
    # this will raise AttributeError if we try to access 'domain' attribute
    #print(geeks.domain)