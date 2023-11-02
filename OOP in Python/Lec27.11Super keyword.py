#  Super keyword
# It refer to the parent class
# It is especially useful when a class inherits from multiple parent classes and you want to call a method from one of the parent classes
# When a class inherits from a parent class, it can override or extend the methods defined in the parent class.

class Employee:
    def __init__(self,name , age):
        self.name = name
        self.age = age

class Programmer(Employee):
    def __init__(self, name, age, lang):
        super().__init__(name, age)
        self.lang = lang
obj1 = Employee("Safi",20)
obj2 = Programmer("Meer", 22 , "Python")

print(obj1.name)
print(obj2.name)