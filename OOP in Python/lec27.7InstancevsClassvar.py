# Instance vs Class variable
# Class variables are defined at the class level and are shared among all instances of the class. 
#  They are defined outside of any method and are usually used to store information that is common to all instances of the class.

# Class variable

class MyClass:
    class_variable = 0
    
    def __init__(self):
        MyClass.class_variable += 1
        
    def print_class_variable(self):
        print(MyClass.class_variable)
        

obj1 = MyClass()
obj2 = MyClass()

obj1.print_class_variable() # Output: 2
obj2.print_class_variable() # Output: 2
# The class_variable is shared among all instances of the class MyClass. When we create new instances of MyClass, the value of class_variable is incremented. When we call the print_class_variable method on obj1 and obj2, we get the same value of class_variable.

# Instance variable
# Instance variables are defined at the instance level and are unique to each instance of the class.
# They are defined inside the init method and are usually used to store information that is specific to each instance of the class


class MyClass:
    def __init__(self, name):
        self.name = name
        
    def print_name(self):
        print(self.name)

obj1 = MyClass("John")
obj2 = MyClass("Jane")

obj1.print_name() # Output: John
obj2.print_name() # Output: Jane

# Each instance of the class MyClass has its own value for the name variable. When we call the print_name method on obj1 and obj2, we get different values for name.



# Example of class to instance variable
class Employee:
    # company name is shareable in class and  known as class variable
    Company_Name= "Microsoft"
    No_of_Employee = 0
    def __init__(self, name):
        self.name = name
        self.raiseAmount = 0.2
        Employee.No_of_Employee += 1
    def Show_Details(self):
        print(f"The name of the Employee is {self.name} and the raise amount is {self.raiseAmount} and sized is {self.No_of_Employee} the company is {self.Company_Name}")

# Employee.Show_Details(emp1)
emp1 = Employee("Safi")
# change the raise amount
emp1.raiseAmount = 0.5
# change class to instance var
emp1.Company_Name= "Google"
emp1.Show_Details()

emp2 = Employee("Khan")
Employee.Company_Name = "Nestle"
emp2.Show_Details()


# Summany
# Class variables are shared among all instances of a class and are used to
#  store information that is common to all instances. Instance variables are 
#   unique to each instance of a class and are used to store information that
#    is specific to each instance. Understanding the difference between class
#      variables and instance variables is crucial for writing efficient and
#          maintainable code in Python.

#It's also worth noting that, in python, class variables are defined outside of
#  any methods and don't need to be explicitly declared as class variable.
#  They are defined in the class level and can be accessed via classname.varibale_name or
#  self.class.variable_name. But instance variables are defined inside the methods
#  and need to be explicitly declared as instance variable by using self.variable_name