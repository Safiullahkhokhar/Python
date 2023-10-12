# if else condition

# userinput= int(input("Enter your age: "))
# print("Your age is: ", userinput)
# if(userinput >= 18):
#     print("You are eligiable for the vote")
# else:
#     print("Not eligiable for the vote")

# >, <, >=, <=, ==, != 

# print(userinput > 18) 
# print(userinput < 18)
# print(userinput >= 18)
# print(userinput <= 18)
# print(userinput == 18)
# print(userinput != 18)

#example 02
applePrice= 20
budget= 200
if(budget-applePrice > 100):
    print("Buy 1 kg apples")
else:
    print("Don't buy apples your budget is low")

# elif condition
num= int(input("Enter the value of number: "))
if(num == 0):
    print("Your number zero")
elif(num == 999):
    print("special number")
elif(num % 2 == 0):
    print("Positive number")
else:
    print("Negative number")

# Nested condition
if(num == 0):
    print("Zero")
elif(num > 0):
    if(num % 2 == 0):
        print("Even number")
    else:
        print("Odd number")
else:
    print("Negative number")


# Short hand statement   if-else in one line

a= 300
b= 400
print('a') if a>b else print('b')
print('A') if a > b else print('=') if a == b else print("B")
# 1. print('A') if a > b
# 2. else print('=') if a == b if 1 and 2 is false than print 3
# 3. else print("B") the output is B

# Syntex
# result = value_if_true if condition else value_if_false

print(9) if a>b else""
c= 9 if a > b else 0
print(c)