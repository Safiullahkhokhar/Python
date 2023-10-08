# Resursion is the process of defining something in terms of itself

#Factorial of 3
def Factorial(x):
    if(x==0 or x==1):
        return 1
    else:
        return x * Factorial(x-1)

num =3
print('This is factorial of', num, 'is', Factorial(num))

#factorial(3)           # 1st call with 3
# 3 * factorial(2)      # 2nd call with 2
# 3 * 2 * factorial(1)  # 3rd call with 1
# 3 * 2 * 1             # return from 3rd call as number=1
# 3 * 2                 # return from 2nd call
# 6                     # return from 1st call


#Resursion limit
import sys  # import sys 

def numbers():
    print(numbers)
    numbers()   
print(sys.getrecursionlimit()) # the resursion limit is 1000

#increse resursion limit 
sys.setrecursionlimit(2000)
print(sys.getrecursionlimit()) #2000


#Fibonacci numbers

def fibo(n):
    a = 0
    b = 1
    # print(a)
    # print(b)


    if n == 1:
        print(a)
    else:
        print(a)
        print(b)

    for i in range(2,n):
        c= a + b
        a=b
        b=c
        print(c)
fibo(10)
