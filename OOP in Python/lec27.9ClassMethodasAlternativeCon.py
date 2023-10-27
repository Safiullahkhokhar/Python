# Class Method as Alternative Constractor
#"constructor" refers to a special type of method that is automatically 
#  executed when an object is created from a class. 
#   The purpose of a constructor is to initialize the object's attributes, 
#    allowing the object to be fully functional and ready to use.

# sometimes when you may want to create an object in a different way, 
#  or with different initial values, than what is provided by the default constructor. 
#   This is where class methods can be used as alternative constructors.

class Person:
    def __init__(self, name, age) :
        self.name = name
        self.age = age
    
    @classmethod
    def from_Str(cls,string):
        name, age= string.split(",")
        return cls(name, int(age))

obj=Person.from_Str("Safiullah,19")
print(obj.name,obj.age)



class Employee:
    # constructor intilize things 
    def __init__(self, name ,salary,company):
        self.name = name
        self.salary = salary
        self.company = company
    
    # A formate of particular data pass 
    @classmethod # use as alternative constructor
    def fromStr(cls, string):
        return cls(string.split('-')[0], string.split('-')[1], string.split('-')[2])
    
e1=Employee("Safiullah",15000, "Google")
print(e1.name)
print(e1.salary)
print(e1.company)

# find out the data from this string
string="Safiullah-20000-Apple"
# if we doing this than code is uggile than we doing class method as alternative constructor like in fronStr()
#e2= Employee(string.split('-')[0], string.split('-')[1], string.split('-')[2])
e2= Employee.fromStr(string)
print(e2.name)
print(e2.salary)
print(e2.company)

