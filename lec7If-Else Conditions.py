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
# if(num == 0):
#     print("Your number zero")
# elif(num == 999):
#     print("special number")
# elif(num % 2 == 0):
#     print("Positive number")
# else:
#     print("Negative number")

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