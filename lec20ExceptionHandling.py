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
