# Decorators 
#decorators are a powerful and versatile tool that allow you to modify 
# the behavior of functions and methods. They are a way to extend the 
#  functionality of a function or method without modifying its source code

# It's a function that takes another function as an argument and returns a 
#  new function that modifies the behavior of the original function. 
#   The new function is often referred to as a "decorated" function

def greet(temfun):
    def mfx(*arg, **dic):
        print("Good morning ")
        temfun(*arg, **dic)
        print("Thanks for using this function")
    return mfx

@greet
def hello():
    print("hello world")

@greet
def add(a,b):
    return a+b

@greet
def sub(a,b):
    return a-b
 
hello()
add(9,1)
sub(5,2)


import logging
def log_fun_cal (func):
    def dec(*tup1,**dic1):
        logging.info(f"calling {func.__name__} wtih tup={tup1}, dic={dic1}")
        result = func(*tup1 , **dic1)
        logging.info(f"{func.__name__} returned {result}")
        return result
    return dec

@log_fun_cal
def fun(a,b):
    return a+b

fun(1,2)


#In conclusion, python decorators are a way to extend the functionality of
#  functions and methods, by modifying its behavior without modifying the source code.
#   They are used for a variety of purposes, such as logging, memoization, access control,
#    and more. They are a powerful tool that can be used to make your code more readable,
#      maintainable, and extendable.