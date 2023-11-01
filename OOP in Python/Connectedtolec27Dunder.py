from typing import Any


class Employee1:
    def __init__(self, name):
        self.name = name
    
#used to get the length of an object. This is useful when you want to be able to find the size of a data structure, such as a list or dictionary.
    def __len__(self):
        i = 0
        for c in self.name:
            i = i + 1
            return i

# __str__ and __repr__ methods
#both used to convert an object to a string representation.
# str method is used when you want to print out an object
    def __str__(self):
        return f"The name of employee is {self.name} str method"

#  repr method is used when you want to get a string representation of an object that can be used to recreate the object    
    def __repr__(self):
        return f"The name of employee is {self.name} repr method"

# used to make an object callable
#meaning that you can pass it as a parameter to a function and it will be executed when the function is called.
    def __call__(self):
        print("I am good")