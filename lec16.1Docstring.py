#Docstings are the string literals that appear right after the defination of a function,method,class or module

def square(n):
    ''' Takes in a number,returns the square of n ''' #not a sting
    print(n ** 2)
square(5)#25
print(square.__doc__)

# PEP 8 (Pyhton Enhancement Proposal) 
# import this