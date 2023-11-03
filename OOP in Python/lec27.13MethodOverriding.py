# Method OverRiding
# allows you to redefine a method in a derived class.
#The method in the derived class is said to override the method in the base class. 
#When you create an instance of the derived class and call the overridden method, the version of the method in the derived class is executed, rather than the version in the base class
# the new implementation must have the same method signature as the original method. This means that the number and type of arguments, as well as the return type, must be the same.
# Another way is to do this, you can use the super function
#The super function allows you to call the base class method from the derived class method, and can be useful when you want to extend the behavior of the base class method, rather than replace it.



class Shape:
    def __init__(self, x , y):
        self.x = x
        self.y =y
    
    def area(self):
        return self.x * self.y

# S = Shape(5,5) # 25
# print(S.area())

class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius
        super().__init__(radius,radius) # x and y name change as radius

    def area(self):
        return 3.14 * super().area() # 3.14 * 25

c= Circle(5)
print(c.area()) # 78.5