# Exception is an unexcepted event that occurs during program execution.
# Error that occur at runtime
# like as: try to open a file that does not exist "FileNotFoundError"
# try to divide a number by zero "ZeroDivisionError"
# try to import a module that does not exist "ImportError"

# Python to handle errors and exceptions. 
# The code in try block runs when there is no error. 
# If the try block catches the error, then the except block is executed.

try:
    num = 10
    denum = 0
    result = num / denum
    print(result)
except:
    print('Error : denum cannot be 0')

#multiple except
try:
    num=int(input('Enter an interger: '))
    a = [6,3]
    print(a[num])
except ValueError:
    print('Number entered is not an integer')
except IndexError:
    print('Index error')

#Table 
a= input('Enter the num for table:')
print(f"Multiplication table of {a} is: ")
try:
    for i in range(1,11):
        print(f"{int(a)} X {i}={int(a)*i}")
except:
    print('invalid input!')

print('some imp lines of code')
print('end of program')

# Finally keyword 
# finally block is always executed no matter whether there is an exception or not.
# The finally block is optional. And, for each try block, there can be only one finally block.
# One of the important use cases of finally block is in a function which returns a value.
# Generally used for doing the concluding tasks like closing file resources or closing database connection or may be ending the program execution with a delightful message.

try:
    num=int(input("Enter your number: "))
except ValueError:
    print("Number entered is not an integer")
else:
    print("Integer Accpected")
finally:
    print("This block os always executed")

# raise custom errors by using the raise keyword
# we can define custom exceptions by creating a new class that is derived from the built-in Exception class
# we may need to create our own custom exceptions that serve our purpose

salary = int(input("Enter  your salary amount: "))
if not 2000 < salary < 5000:
    raise("Not a vaild salary")

x= 'hello'
if not type(x) is int:
    raise TypeError('Only integers are allowed')