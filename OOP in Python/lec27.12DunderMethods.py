# Dunder Methods
# Special methods that you can define in your classes, and when invoked, they give you a powerful way to manipulate objects and their behaviour.
# Powerful tools that allow you to customize the behaviour of your classes
# They are used to implement special methods such as the addition, subtraction and comparison operators, as well as some more 
#  advanced techniques like descriptors and properties


# __init__ or constructor
#The init method is a special method that is automatically invoked when you create a new instance of a class. 
#This method is responsible for setting up the object’s initial state, and it is where you would typically define any instance variables that you need

# class Employee:
#     def __init__(self, name):
#         self.name = name
# obj1= Employee("Safi")
# print(obj1.name)


from Connectedtolec27Dunder import Employee1

e = Employee1("Harry")
#print(e)
print(str(e))
print(repr(e))
e()