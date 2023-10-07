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

