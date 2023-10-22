# These all are conventions
# Access Modifiers
# Used to limit the access of class variables and
#  class methods outside of class while implementing the concepts of inheritance.

# Public 
# All the variables and methods (member functions) in python are by default public.
# Any instance variable in a class followed by the ‘self’ keyword ie. self.var_name are public accessed.
class A:
    def __init__(self):
        self.name= "safi"
objp = A()
print(objp.name)

# Privite

# In Python, there is no strict concept of "private" access modifiers
#  like in some other programming languages.
#    However, a convention has been established to indicate that a
#     variable or method should be considered private by prefixing its name
#       with a double underscore (__). This is known as a "weak internal use indicator"
#        and it is a convention only, not a strict rule. 
# Code outside the class can still access these "private" variables and methods, but it is generally understood that they should not be accessed or modified.

class Pri:
    def __init__(self):
        self.__name = "safiullah" # indication prefixing underscore (__)
obj= Pri()
#print(objP.__name) # Cannot be access directly
print(obj._Pri__name) # can be accessed indirectly is known as "name mangling"

# Name Mangling

# Its a technique used to protect class-private and superclass-private attributes from being accidentally overwritten by subclasses.
# Names of class-private and superclass-private attributes are transformed by the addition of a single leading underscore and a double leading underscore respectively

class NM:
    def __init__(self):
        self._nonmangledAttribute = "I am a nonmangled attribute"
        self.__mangledAttribute = "I am a mangled attribute"
objNM= NM()
print(objNM._nonmangledAttribute)
print(objNM._NM__mangledAttribute)

# Protected
# "protected" is used to describe a member (i.e., a method or attribute) of a class that is intended to be accessed only by the class itself and its subclasses.
#   In Python, the convention for indicating that a member is protected is to prefix its name with a single underscore (_)

# It's important to note that the single underscore is just a naming convention, 
# and does not actually provide any protection or restrict access to the member. 
# The syntax we follow to make any variable protected is to write variable name 
# followed by a single underscore (_) ie. _varName.