# Methods for object introexception
# dir(), help(),_dict_

# dir() method
#  returns a list of all the attributes and methods (including dunder methods) available for an object
#  It is a useful tool for discovering what you can do with an object.
a = [ 1 ,2, 2]
print(dir(a))
print(a.__add__) # it shows the output <method-wrapper 

# Tuple
b = (1,2,3)
print(dir(b)) 

# __dict__ Dunder
# attribute returns a dictionary representation of an object's attributes. It is a useful tool for introspection.
class Person:
    def __init__(self, name , age) :
        self.name = name
        self.age = age

obj = Person("Ali",30)
print(obj.__dict__)

# output is {'name': 'Ali', 'age': 30}

# help() method
# used to get help documentation for an object, including a description of its attributes and methods.
#print(help(str))
print(help(int))
# output is 
# Help on class int in module builtins:
# class int(object)
#  |  int([x]) -> integer
#  |  int(x, base=10) -> integer
#  |
#  |  Convert a number or string to an integer, or return 0 if no arguments
#  |  are given.  If x is a number, return x.__int__().  For floating point
#  |  numbers, this truncates towards zero.
#  |
#  |  If x is not a number or if base is given, then x must be a string,
#  |  bytes, or bytearray instance representing an integer literal in the
#  |  given base.  The literal can be preceded by '+' or '-' and be surrounded
#  |  by whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.
