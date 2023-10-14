# local v/s global variable

# local variable is a variable that is defined within a function and is only accessible within that functions.
# It's only created when the function is called and is destroyes when the function returns.

def hello():
    l=10
    print(f"this is local variable {l}")
hello()

# globle variable that is defined outside of a function and is accessible from within any function in your code.

g=5
print(f"this is a global variable {g}")

# change the global variable value in funcation using global keyword

def cha_value():
    global g
    g= 12
    l=10
    print(f"In function local variable {l}, changed value of global variable {g}")
cha_value()
print(f"Value changed of a globle variable {g}")
