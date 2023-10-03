# while loop execute statement while the condition becomes False.

i = 1 ## i is a variable initilaze with with 1 
while (i <= 5): # Enter in while loop if condition Ture than execute the body of the loop
    print(i)    # print the value of i 
    i= i+1 # adding 1       print 0 to 5

j = 5
while (j > 0):
    print(j)
    j= j -1 # print 5 to 1

# frome the user input

# k = int(input("Enter the number: ")) # taking user input <= 40 than execute the while loop otherwisw print message loop teminated
# print(k)
# while (k <= 40):
#     k = int(input("Enter the number: ")) # taking user input from inside the while loop
#     print(k)
# print("the loop terminated")

# using else in while loop

x = 1
while(x <= 5):
    print(x)
    x = x+1
else:
    print("I am in else \n")

while True:
    num= int(input("Enter positive number: "))
    print(num)
    if not num > 0: 
        break

# not keyword is a powerful tool that can be used to control the flow of execution in Python programs
#not keyword is used to check if the number that the user entered is not greater than zero. If the number is not greater than zero, the loop breaks. This ensures that the program only prints positive numbers.
