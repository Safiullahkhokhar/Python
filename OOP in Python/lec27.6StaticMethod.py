# Static Method
# Static methods in Python are methods that belong to a class rather than an instance of the class. 
# They are defined using the @staticmethod decorator and do not have access to the instance of the class (i.e. self)
# They are called on the class itself, not on an instance of the class. Static methods are often used to create utility functions that don't need access to instance data.

class Math:
    def __init__(self , num):
        self.num = num

    def add2Num(self , n):
        self.num = self.num + n

    @staticmethod
    def add( a , b ):
        return a + b
obj=Math(5)
print("value of num",obj.num)
obj.add2Num(2)
print("2 is added now total is:",obj.num)
print("static method ",Math.add(2,6))

# The add method is a static method of the Math class. 
#  It takes two parameters a and b and returns their sum. 
#   The method can be called on the class itself, 
#    without the need to create an instance of the class.


