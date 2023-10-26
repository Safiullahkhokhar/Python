# Class Methods
# A class method is a type of method that is bound to the class and
#  not the instance of the class. In other words, it operates on the class as a whole,
#   rather than on a specific instance of the class. Class methods are defined using the 
#    "@classmethod" decorator, followed by a function definition. The first argument of the function
#        is always "cls," which represents the class itself.

class Employee:
    # class variable
    company_Name = "Google"
    
    def show(self):
        print(f"The name of employee is {self.name} and company is {self.company_Name}")
    
    # cls reference to the class so I add a @classmethod decorator this decorato helps to edit the class directly "newcompname" will changed and get 1st argument by-default as a instance 
    @classmethod
    def changecompnam(self, newcompname): 
    # it take 1st argument as object and in that object it set a company with newcompname  and where change the name of "self" 
        self.company_Name = newcompname

obj = Employee()
obj.name ="Safiullah"
obj.show()
# change company name
obj.changecompnam("Apple")
obj.show()
# 
print(Employee.company_Name)