# This explores the basics of Python that I am learning right now. #
# @author Omar Barazanji                                           #
# @version 2018                                                    #
####################################################################

# This is how you declare and print primative data types
mystring = "Omar"
myint = 20
myfloat = 20.0
print(mystring)
print(myint)
print(myfloat)

# This is how you declare params
a, b, c, d = 3, 4, 5, 6
print(a, b, c, d)

# This is a list (similar to Arrays in Java)
mylist = []
mylist.append(1) #this is how you add to the list
mylist.append(2)
mylist.append(3)
print(mylist[0]) #this is how you print / call for an element in a list
print(mylist[1])
print(mylist[2])

# This is for-each loop syntax printing the list above
for x in mylist:
    print(x)
    
# Arithmetic is the same as it would be in Java, but check this out
squared = 7 ** 2 #two multiplication symbols means "to the power of"
cubed = 7 ** 3
print(squared)
print(cubed)

# You can combine lists by adding them!
even_numbers = [2, 4, 6, 8]
odd_numbers = [1, 3, 5, 7]
all_numbers = odd_numbers + even_numbers
print(all_numbers)

# You can print a list multiple times by using this syntax
print([1, 2, 3] * 3)
print(mylist * 3)

# %s prints a string, %d prints a decimal (int), and %f prints a float
print("Hello %s!" % mystring)
print("%s is %d years old." % (mystring, myint))
print("%s is %f years old." % (mystring, myfloat))
print("A list: %s" % mylist) #You can print lists using %s

# Check this syntax out:
data = ("John", "Doe", 53.44)
format_string = "Hello %s %s. Your current balance is $%s."
print(format_string % data)

# Classes and Method/Function syntax
class MyClass:
    variable = "blah"

    def function(self):
        print("This is a message inside the class.")
myobject = MyClass()
myobject.function()

# This is a dictionary (data type similar to arrays, 
#but uses keys and values instead of indexes)
phonebook = {}
phonebook["John"] = 3348037574
phonebook["Jack"] = 3348037573
phonebook["Jill"] = 3348037572
print(phonebook)

# Iterating through a dictionary
for name, number in phonebook.items():
    print("Phone number of %s is %d" % (name, number))

# Deleting a dictionary entry
del phonebook["John"]
print(phonebook)
# OR
phonebook.pop("Jill")
print(phonebook)

# This is how you use the numpy library (downloaded from git)
import numpy as np
List_A = np.array([34.4, 77.7])
List_B = np.array([234.4, 99.0])
print(List_A)
print(List_B)
print(List_A * List_B)
